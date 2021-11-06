let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 34, lng: -118 },
    zoom: 4,
  });
  // console.log("hello1");
  console.log(locations);
  // console.log("hello2");
  for (var i in locations) {
    marker = new google.maps.Marker({
      position: { lat: locations[i]["lat"], lng: locations[i]["long"] },
      map: map,
    });
  }
}

function createMarker(latitude, longitude) {
  marker = new google.maps.Marker({
    position: { lat: latitude, lng: longitude },
    map: map,
  });
}
