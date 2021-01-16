//GET ACTUAL POSITION 
console.log( "document loaded" );
var x = document.getElementById("bloque");
var lat = '';
var long = '';

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
}


function showPosition(position) {
    x.innerHTML = "<h3 class='latitude'>Latitude: " + position.coords.latitude + 
    "</h3><h3 class='longitude'>Longitude: " + position.coords.longitude + "</h3>";
    lat = position.coords.latitude;
    long = position.coords.longitude;

}

// CHARGE GOOGLE MAP


//document.addEventListener('DOMContentLoaded', Function() {initMap()})
let map;

function initMap() {
  
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: new google.maps.LatLng(lat, long),
    mapTypeId: "terrain",
  });
  // Create a <script> tag and set the USGS URL as the source.
  const script = document.createElement("script");
  // This example uses a local copy of the GeoJSON stored at
  // http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp
  script.src =
    "https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js";
  document.getElementsByTagName("head")[0].appendChild(script);
  console.log("Latitud= " + lat + ", Longitud= " + long);
}

// Loop through the results array and place a marker for each
// set of coordinates.
/*const eqfeed_callback = function (results) {
  for (let i = 0; i < results.features.length; i++) {
    const coords = results.features[i].geometry.coordinates;
    const latLng = new google.maps.LatLng(coords[1], coords[0]);
    new google.maps.Marker({
      position: latLng,
      map: map,
    });
  }
};*/