onload = function() {

var btn = document.getElementById("ledon");
btn.addEventListener("click", switchon);

function switchon() {
  window.location = "/ledtoggle?status=off";
}

}
