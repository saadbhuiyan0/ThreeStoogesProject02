var mymap = L.map('mapid', {
    center: [51.505, -0.09],
    zoom: 6 
});
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'pk.eyJ1IjoiYmF2cmFoYW1pIiwiYSI6ImNrNWVrNThzZjAwbTUzanFvcmNmdmE0eGIifQ.FxbX7od1AfbBYC_dPK0a-A'
}).addTo(mymap);

var pointer = L.marker([51.505,-0.09]);

pointer.addTo(mymap);
