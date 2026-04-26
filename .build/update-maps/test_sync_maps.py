"""
Black-box tests for sync_maps.py.

Tests operate on the public functions using realistic inputs, verifying
file outputs rather than internal state.
"""
import os
import tempfile
import pytest
from sync_maps import generate_slug, build_front_matter, sync_maps, render_front_matter


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_map(
    map_name="Test Map",
    download_url="https://example.com/map.zip",
    preview_url="https://example.com/preview.png",
    description="A test map.",
    size=12345,
    last_commit=1700000000000,
):
    return {
        "mapName": map_name,
        "downloadUrl": download_url,
        "previewImageUrl": preview_url,
        "description": description,
        "downloadSizeInBytes": size,
        "lastCommitDateEpochMilli": last_commit,
        "mapTags": None,
    }


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_map_file(path):
    """Splits a generated map file into front-matter lines and body."""
    content = read_file(path)
    parts = content.split("---\n")
    # parts[0] is empty, parts[1] is front-matter, parts[2] is body
    front_matter_lines = parts[1].strip().splitlines()
    body = parts[2]
    front_matter = {}
    for line in front_matter_lines:
        key, _, value = line.partition(": ")
        front_matter[key.strip()] = value.strip().strip("'")
    return front_matter, body


# ---------------------------------------------------------------------------
# Slug generation
# ---------------------------------------------------------------------------

class TestGenerateSlug:
    def test_spaces_become_dashes(self):
        assert generate_slug("Big World") == "big-world"

    def test_underscores_become_dashes(self):
        assert generate_slug("big_world") == "big-world"

    def test_mixed_case_lowercased(self):
        assert generate_slug("BigWorld") == "bigworld"

    def test_special_characters_stripped(self):
        assert generate_slug("270BC: Wars!") == "270bc-wars"

    def test_numbers_preserved(self):
        assert generate_slug("1914-cow-empires") == "1914-cow-empires"

    def test_multiple_dashes_kept(self):
        # Consecutive dashes from e.g. "A & B" should not crash
        slug = generate_slug("A & B")
        assert slug == "a--b"

    def test_all_special_chars_stripped(self):
        result = generate_slug("Hello (World)")
        assert result == "hello-world"


# ---------------------------------------------------------------------------
# Front-matter field mapping
# ---------------------------------------------------------------------------

class TestBuildFrontMatter:
    def test_img_mapped_from_preview_url(self):
        m = make_map(preview_url="https://example.com/img.png")
        fm = build_front_matter(m)
        assert fm["img"] == "https://example.com/img.png"

    def test_title_format(self):
        m = make_map(map_name="Big World")
        fm = build_front_matter(m)
        assert fm["title"] == "Big World | TripleA Map"

    def test_slug_generated_from_map_name(self):
        m = make_map(map_name="Big World")
        fm = build_front_matter(m)
        assert fm["slug"] == "big-world"

    def test_download_url_preserved(self):
        m = make_map(download_url="https://example.com/archive.zip")
        fm = build_front_matter(m)
        assert fm["downloadUrl"] == "https://example.com/archive.zip"

    def test_size_included(self):
        m = make_map(size=99999)
        fm = build_front_matter(m)
        assert fm["downloadSizeInBytes"] == 99999

    def test_last_commit_included(self):
        m = make_map(last_commit=1700000000000)
        fm = build_front_matter(m)
        assert fm["lastCommitDateEpochMilli"] == 1700000000000

    def test_no_map_category_field(self):
        m = make_map()
        fm = build_front_matter(m)
        assert "mapCategory" not in fm

    def test_no_version_field(self):
        m = make_map()
        fm = build_front_matter(m)
        assert "version" not in fm

    def test_null_size_omitted(self):
        m = make_map()
        m["downloadSizeInBytes"] = None
        fm = build_front_matter(m)
        assert "downloadSizeInBytes" not in fm


# ---------------------------------------------------------------------------
# File output
# ---------------------------------------------------------------------------

class TestSyncMaps:
    def test_one_file_written_per_map(self):
        with tempfile.TemporaryDirectory() as d:
            maps = [make_map("Map A"), make_map("Map B"), make_map("Map C")]
            result = sync_maps(maps, d)
            assert result["written"] == 3
            assert len(os.listdir(d)) == 3

    def test_filename_matches_slug(self):
        with tempfile.TemporaryDirectory() as d:
            sync_maps([make_map("Big World")], d)
            assert os.path.exists(os.path.join(d, "big-world.html"))

    def test_description_written_as_body(self):
        with tempfile.TemporaryDirectory() as d:
            sync_maps([make_map(description="<br>Some description\n")], d)
            _, body = parse_map_file(os.path.join(d, "test-map.html"))
            assert "Some description" in body

    def test_null_description_does_not_crash(self):
        with tempfile.TemporaryDirectory() as d:
            m = make_map()
            m["description"] = None
            sync_maps([m], d)
            assert os.path.exists(os.path.join(d, "test-map.html"))

    def test_missing_description_does_not_crash(self):
        with tempfile.TemporaryDirectory() as d:
            m = make_map()
            del m["description"]
            sync_maps([m], d)
            assert os.path.exists(os.path.join(d, "test-map.html"))

    def test_stale_files_removed(self):
        with tempfile.TemporaryDirectory() as d:
            # Write an old file that won't be in the new listing
            stale = os.path.join(d, "old-map.html")
            with open(stale, "w") as f:
                f.write("stale")

            sync_maps([make_map("New Map")], d)

            assert not os.path.exists(stale)
            assert result_count(d) == 1

    def test_removed_count_returned(self):
        with tempfile.TemporaryDirectory() as d:
            for name in ["stale-a.html", "stale-b.html"]:
                open(os.path.join(d, name), "w").close()

            result = sync_maps([make_map("Fresh Map")], d)
            assert result["removed"] == 2

    def test_idempotent(self):
        """Running twice with the same input produces identical file contents."""
        maps = [make_map("Big World"), make_map("Classic")]
        with tempfile.TemporaryDirectory() as d:
            sync_maps(maps, d)
            contents_first = {
                f: read_file(os.path.join(d, f)) for f in os.listdir(d)
            }
            sync_maps(maps, d)
            contents_second = {
                f: read_file(os.path.join(d, f)) for f in os.listdir(d)
            }
            assert contents_first == contents_second

    def test_front_matter_fields_in_output(self):
        with tempfile.TemporaryDirectory() as d:
            sync_maps([make_map("My Map", preview_url="https://img.example.com/p.png")], d)
            fm, _ = parse_map_file(os.path.join(d, "my-map.html"))
            assert fm["mapName"] == "My Map"
            assert fm["slug"] == "my-map"
            assert "img.example.com" in fm["img"]
            assert fm["title"] == "My Map | TripleA Map"


def result_count(directory):
    return len([f for f in os.listdir(directory) if f.endswith(".html")])

