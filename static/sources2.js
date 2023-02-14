var earthquakes;

var geo_data = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-01-01&endtime=2023-02-01&minmagnitude=3&eventtype=earthquake&minlatitude=32.5&minlongitude=-124.5&maxlatitude=42.0&maxlongitude=-114.0'

// Perform a GET request to the query URL/
d3.json(geo_data).then(function (data) {
    // Once we get a response, send the data.features object to the createFeatures function.
    createFeatures(data.features);
  });
  
function createFeatures(earthquakeData) {

    function onEachFeature(feature, layer) {
      //layer.bindPopup(`<h3>${feature.properties.place}</h3><hr><p>${new Date(feature.properties.time)}</p>`);
      layer.bindPopup(`<h3>${feature.properties.place}</h3><hr><p>${new Date(feature.properties.time)}</p><p>Latitude: ${feature.geometry.coordinates[1]}, Longitude: ${feature.geometry.coordinates[0]}</p>`);
    }
  
    earthquakes = L.geoJSON(earthquakeData, {
      onEachFeature: onEachFeature
    });
  
    createMap(earthquakes);
}

function createMap(earthquakes) {

    var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })
  
    var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });
  
    var baseMaps = {
      "Street Map": street,
      "Topographic Map": topo
    };
  
    var overlayMaps = {
      Earthquakes: earthquakes
    };
  
    var myMap = L.map("map", {
      center: [
        37.09, -95.71
      ],
      zoom: 5,
      layers: [street, earthquakes]
    });

    // Get the bounds of the earthquakes layer
    var bounds = earthquakes.getBounds();
  
    // Fit the map to the bounds of the earthquakes layer
    myMap.fitBounds(bounds);
  
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);
  
}

var slider = document.getElementById("yearSlider");
var yearValue = document.getElementById("yearValue");

slider.addEventListener("input", function() {
  var year = this.value;
  yearValue.innerHTML = year; // Update the yearValue element with the current value
  var url = `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=${year}-01-01&endtime=${year}-12-31&minmagnitude=3&eventtype=earthquake&minlatitude=32.5&minlongitude=-124.5&maxlatitude=42.0&maxlongitude=-114.0`
  d3.json(url).then(function (data) {
    // Clear the earthquakes layer
    earthquakes.clearLayers();
    // Add the new data to the earthquakes layer
    earthquakes.addData(data.features);
  });
});

