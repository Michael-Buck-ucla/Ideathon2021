let map, infoWindow;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 34, lng: -118 },
    zoom: 4,
  });
  console.log("hi");
  console.log(locations);
  for (const [key, value] of Object.entries(locations)) {
    const marker = new google.maps.Marker({
      position: { lat: value["lat"], lng: value["long"] },
      map: map,
      title: key,
    });
    console.log(key);
    // console.log(locations[i]["lat"]);

    marker.addListener("click", () => {
      infoWindow.close();
      //infoWindow.setContent(locations[i]["lat"]);
      //infoWindow.open(marker.getMap(), marker);

      var para = document.getElementById("event"); // Create a <p> element
      para.innerText = marker.getTitle(); // Insert text
      // document.body.appendChild(para);
    });
  }

  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  const uclaMarker = new google.maps.Marker({
    position: { lat: 34, lng: -118 },
    map: map,
  });

  locationButton.textContent = "Pan to Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          const image =
            "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
          const beachMarker = new google.maps.Marker({
            position: pos,
            map,
            icon: image,
          });

          infoWindow.setPosition(pos);
          infoWindow.setContent("Location found.");
          infoWindow.open(map);

          map.setCenter(pos);
          map.setZoom(15);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}
