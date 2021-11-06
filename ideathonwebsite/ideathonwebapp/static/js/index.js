let map, infoWindow;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 4,
  });

  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  const uclaMarker = new google.maps.Marker({
    		position: { lat: 34, lng: -118 },
    		map: map,
  	      });

  uclaMarker.addListener("click", () => {
      infoWindow.close();
      infoWindow.setContent("blmsfkls");
      infoWindow.open(uclaMarker.getMap(), uclaMarker);

      var para = document.createElement("P");               // Create a <p> element
	  para.innerText = "This is a paragraph";               // Insert text
	  document.body.appendChild(para);
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

          const image = "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
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
