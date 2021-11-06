let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 34, lng: -118 },
    zoom: 4,
  });

  for (var i in locations) {
    marker = new google.maps.Marker({
      position: { lat: locations[i]["lat"], lng: locations[i]["long"] },
      map: map,
    });
  }
}
