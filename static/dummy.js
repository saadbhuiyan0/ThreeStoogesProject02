var lat=document.getElementById("lat").innerHTML
var lon=document.getElementById("lon").innerHTML
var clat=document.getElementById("clat").innerHTML
var clon=document.getElementById("clon").innerHTML
var zoom=document.getElementById("zoom").innerHTML


var mymap = L.map('mapid', {
  center: [lat, lon],
  zoom: zoom,
  minZoom: zoom,
  maxZoom: zoom,
  dragging: false
});


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  accessToken: 'pk.eyJ1IjoiYmF2cmFoYW1pIiwiYSI6ImNrNWVrNThzZjAwbTUzanFvcmNmdmE0eGIifQ.FxbX7od1AfbBYC_dPK0a-A'
}).addTo(mymap);


var pointer = L.marker([clat, clon]);
var textOptions = [
  "There's a great place here!",
  "I think you'll enjoy this location.",
  "Have you considered this option?",
  "This is one of my favorites!",
  "Here you go, enjoy!"
]
var randomIndex = Math.floor(Math.random() * textOptions.length); 
pointer.bindPopup(textOptions[randomIndex])
var onmap = false;


var addpopup = function(e) {
  if (onmap == false) {
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
