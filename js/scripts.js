function hideShowInstallationText(which) {
  [].forEach.call(document.getElementsByClassName("installation-instructions"), function(current){
    if(current !== which){
      current.style.display="none";
    }
  });
  if(which){
    which.style.display="block";
  }
}
