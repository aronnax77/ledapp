onload = function() {

var btn = document.getElementById("ledoff");
btn.addEventListener("click", switchoff);

function switchoff() {
  window.location = "/ledtoggle?status=on";
}

}
