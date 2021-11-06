let map, infoWindow;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 34, lng: -118 },
    zoom: 4,
  });

  for (const [key, value] of Object.entries(locations)) {
    const marker = new google.maps.Marker({
      position: { lat: value["lat"], lng: value["long"] },
      map: map,
      title: key,
    });
    //console.log(key);
    // console.log(locations[i]["lat"]);

    marker.addListener("click", () => {
      infoWindow.close();

      var theName = marker.getTitle();
      document.getElementById("title").innerText = theName;
      document.getElementById("host").innerText =
        "Host: " + locations[theName]["host"];
      document.getElementById("start").innerText =
        "Start Time: " + locations[theName]["start"];
      document.getElementById("end").innerText =
        "End Time: " + locations[theName]["end"];
      document.getElementById("genre").innerText =
        "Genre: " + locations[theName]["genre"];
      document.getElementById("num").innerText =
        "Number of Attendees: " + locations[theName]["num"];
      document.getElementById("cost").innerText =
        "Entry Cost: " + locations[theName]["cost"];
      document.getElementById("age").innerText =
        "Age Range: " + locations[theName]["age"];
    });
  }

  infoWindow = new google.maps.InfoWindow();

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

        //infoWindow.setPosition(pos);
        //infoWindow.setContent("Location found.");
        //infoWindow.open(map);

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
