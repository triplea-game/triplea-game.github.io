function hideShowInstallationText(which) {
  if (!document.getElementById) {
    return;
  }
  if (which.style.display=="block") {
    which.style.display="none";
  }
  else {
    which.style.display="block";
  }
}
if (typeof String.prototype.endsWith !== 'function') {
    String.prototype.endsWith = function(suffix) {
      return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}
function setLink(url, size){
  var id = null;
  if(url.endsWith("64bit.exe")){
    id = "win64";
  } else if(url.endsWith("32bit.exe")){
    id = "win32";
  } else if(url.endsWith("macos.dmg")){
    id = "macos";
  } else if(url.endsWith("unix.sh")){
    id = "linux";
  }
  if(id !== null){
    document.getElementById(id).href = url;
    document.getElementById(id).addEventListener("mouseover", function(){
      document.getElementById("dl-size-mb").innerHTML = Math.round(10 * size / (1024 * 1024)) / 10;
    });
  }
}
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
  if(this.status == 200 && this.readyState == 4){
    var releases = JSON.parse(this.responseText);
    for(var i = 0; i < releases.length; i++){
      if(!releases[i]['prerelease']){
        releases[i]['assets'].forEach(function(currentAsset){
          setLink(currentAsset['browser_download_url'], currentAsset['size']);
        });
        break;
      }
    }
  }
};
xhttp.open("GET", "https://api.github.com/repos/triplea-game/triplea/releases", true);
xhttp.send();
