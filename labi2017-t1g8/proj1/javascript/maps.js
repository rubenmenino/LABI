function initMap() {
  var uluru = {lat: 40.6439048, lng: -8.6515456};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: uluru,
  });
  
  var marker = new google.maps.Marker({
    position: uluru,
    map: map,
    icon: 'img/marker.png'
  });
  
}