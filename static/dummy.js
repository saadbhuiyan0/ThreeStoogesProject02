//var mymap = L.map('mapid', {
//  center: [51.505, -0.09],
//  zoom: 6 
//});

var mymap = L.map('mapid').setView([51.505, -0.09], 6);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  accessToken: 'pk.eyJ1IjoiYmF2cmFoYW1pIiwiYSI6ImNrNWVrNThzZjAwbTUzanFvcmNmdmE0eGIifQ.FxbX7od1AfbBYC_dPK0a-A'
}).addTo(mymap);

var pointer = L.marker([51.505,-0.09]);
pointer.bindPopup("You can find it here.")
var onmap = false;

var addpopup = function(e) {
  console.log(onmap);
  if (onmap == false) {
    console.log("a");
    pointer.addTo(mymap);
    onmap = true;
  }
  pointer.openPopup();
}

var removepopup = function(e) {
  if (onmap == true) {
    pointer.remove();
    onmap = false;
  }
}

var lis = document.getElementsByClassName("addpointer");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('click', addpopup);
}

var cl = document.getElementById("removepointer");
cl.addEventListener('click',removepopup);
