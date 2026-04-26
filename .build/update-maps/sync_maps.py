#!/usr/bin/env python3
"""
Fetches the map listing from the TripleA server and regenerates the Jekyll
map pages in _maps/. Each map in the JSON response becomes one .html file
with YAML front-matter and an HTML description body.

Usage:
    python3 sync_maps.py [--maps-dir PATH] [--url URL]
"""
import argparse
import json
import os
import re
import sys
import urllib.request

MAPS_LISTING_URL = "https://prod.triplea-game.org/support/maps/listing"


def generate_slug(map_name: str) -> str:
    """Converts a map name to a URL-safe slug used as the filename."""
    slug = map_name.lower()
    slug = slug.replace(" ", "-").replace("_", "-")
    slug = re.sub(r"[^a-z0-9\-]", "", slug)
    return slug


def build_front_matter(map_data: dict) -> dict:
    """
    Transforms a single map dict from the API into the YAML front-matter
    fields written to the Jekyll page.
    """
    slug = generate_slug(map_data["mapName"])
    front_matter = {
        "mapName": map_data["mapName"],
        "slug": slug,
        "title": f"{map_data['mapName']} | TripleA Map",
        "downloadUrl": map_data.get("downloadUrl", ""),
        "img": map_data.get("previewImageUrl", ""),
    }
    if map_data.get("downloadSizeInBytes") is not None:
        front_matter["downloadSizeInBytes"] = map_data["downloadSizeInBytes"]
    if map_data.get("lastCommitDateEpochMilli") is not None:
        front_matter["lastCommitDateEpochMilli"] = map_data["lastCommitDateEpochMilli"]
    return front_matter


def render_front_matter(fields: dict) -> str:
    """Serializes a dict to a YAML front-matter block without pulling in PyYAML."""
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, str):
            # Quote strings that contain characters that could confuse YAML parsers.
            if any(c in value for c in (':', '#', '[', ']', '{', '}', '&', '*', '!', '|', '>', "'", '"')):
                escaped = value.replace("'", "''")
                lines.append(f"{key}: '{escaped}'")
            else:
                lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def write_map_file(target_dir: str, map_data: dict) -> str:
    """
    Writes one Jekyll map page and returns the file path written.
    The description from the API becomes the page body below the front-matter.
    """
    front_matter = build_front_matter(map_data)
    slug = front_matter["slug"]
    description = map_data.get("description") or ""

    content = render_front_matter(front_matter) + description.strip() + "\n"

    file_path = os.path.join(target_dir, f"{slug}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path


def sync_maps(maps: list, target_dir: str) -> dict:
    """
    Clears target_dir and writes one .html file per map entry.
    Returns a summary dict with counts of files written and removed.
    """
    existing_files = set(
        f for f in os.listdir(target_dir) if f.endswith(".html")
    )

    written_files = set()
    for map_data in maps:
        path = write_map_file(target_dir, map_data)
        written_files.add(os.path.basename(path))

    stale_files = existing_files - written_files
    for filename in stale_files:
        os.remove(os.path.join(target_dir, filename))

    return {
        "written": len(written_files),
        "removed": len(stale_files),
    }


def fetch_maps(url: str) -> list:
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Sync TripleA map pages from server listing.")
    parser.add_argument("--maps-dir", default="_maps", help="Path to the _maps directory")
    parser.add_argument("--url", default=MAPS_LISTING_URL, help="Maps listing JSON URL")
    args = parser.parse_args()

    maps_dir = args.maps_dir
    if not os.path.isdir(maps_dir):
        print(f"Error: '{maps_dir}' is not a directory", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching map listing from {args.url} ...")
    maps = fetch_maps(args.url)
    print(f"Fetched {len(maps)} maps.")

    result = sync_maps(maps, maps_dir)
    print(f"Done. Written: {result['written']}, Removed: {result['removed']}")


if __name__ == "__main__":
    main()

