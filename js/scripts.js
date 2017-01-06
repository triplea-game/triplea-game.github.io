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
