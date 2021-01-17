//GET ACTUAL POSITION
var x = document.getElementById('bloque');
var map, lat, lng, infoWindow;

// Centrar mapa de ser posible al inicio
document.addEventListener('DOMContentLoaded', () => {
  if (navigator.geolocation) {
    try {
      centrarMapa();
    } catch (error) {
      console.error(error);
    }
  }
});

// Coordenadas genericas de Santiago si el usuario no quiere dar geolocalizacion
lat = -33.44950792242694;
lng = -70.66775128317754;
showPosition(undefined, lat, lng);
// farmaciasCercanas(lat, lng);

//creacion e inicio del mapa
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: new google.maps.LatLng(lat, lng),
    mapTypeId: 'roadmap',
  });
  console.log('Latitud= ' + lat + ', Longitud= ' + lng);

  infoWindow = new google.maps.InfoWindow();
  const locationButton = document.createElement('button');
  locationButton.textContent = 'Centrar en tu ubicación';
  locationButton.classList.add('custom-map-control-button');
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener('click', () => {
    centrarMapa();
  });
}

// agrega marker en el mapa con parámetro elemento farmacia.json
function agregarMarker(farmacia) {
  console.log(farmacia);

  const lat = farmacia['local_lat'];
  const lng = farmacia['local_lng'];
  const title = farmacia['local_nombre'];
  const contentString = `<div><h1 class="nombre">${farmacia['local_nombre']}</h1></div><div>    <p>Dirección: ${farmacia['local_direccion']}, ${farmacia['comuna_nombre']}</p></div><div>    <p>Fono: ${farmacia['local_telefono']}</p></div><div>    <p>Horario Turno: ${farmacia['funcionamiento_dia']} ${farmacia['fecha']} de ${farmacia['funcionamiento_hora_apertura']} a ${farmacia['funcionamiento_hora_cierre']}</p></div>`;

  const infowindow = new google.maps.InfoWindow({
    content: contentString,
  });
  const latLng = new google.maps.LatLng(lat, lng);
  const marker = new google.maps.Marker({
    position: latLng,
    map: map,
    title: title,
  });

  marker.addListener('click', () => {
    infowindow.open(map, marker);
  });
}

// Centra mapa si el usuario lo permite
function centrarMapa() {
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
        console.log(pos);
        showPosition(position);
        infoWindow.setPosition(pos);
        infoWindow.setContent('Estás aquí');
        infoWindow.open(map);
        map.setCenter(pos);

        console.log(
          `coordenadas a las cuales es esta corriendo ${lat}, ${lng} `
        );
        
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

// Manejo de error de acuerdo a la documentacion de Google
function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? 'Error: El servicio de Geolocalización falló.'
      : 'Error: Favor ingresar dirección en la barra o autorizar localización.'
  );
  infoWindow.open(map);
}

// Indica posicion en el front
function showPosition(position = false, lat = false, long = false) {
  if (position) {
    x.innerHTML =
      "<h4 class='latitude'>Latitude: " +
      position.coords.latitude +
      "</h4><h4 class='longitude'>Longitude: " +
      position.coords.longitude +
      '</h4>';
  } else {
    x.innerHTML =
      "<h3 class='latitude'>Latitude: " +
      lat +
      "</h3><h3 class='longitude'>Longitude: " +
      long +
      '</h3>';

  }
  farmaciasCercanas(position.coords.latitude, position.coords.longitude);
  fetchClima(position.coords.latitude, position.coords.longitude);
  fetchFase(position.coords.latitude, position.coords.longitude);
}

// hace el fetch del listado de farmacias cercanas del backend
function farmaciasCercanas(latitud, longitud) {
  fetch(`../farmacias/${latitud}/${longitud}`)
    // fetch('https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos')
    .then((response) => response.json())
    .then((farmacias) => {
      console.log(
        `se esta corriendo farmaciascercanas con ${latitud},${longitud}`
      );
      farmacias.forEach((farmacia) => agregarMarker(farmacia));
    });
}

// funcion para conseguir el clima dependiento la ubicacion
// si se va a usar con coordenadas usar asi fetchClima(lat, lng)
// si se va a usar con direccion usar asi fetchClima(undefined, undefined, direccion)
function fetchClima(latitud, longitud, direccion = false) {
  var clima = document.getElementById('tiempo');
  
  let url;
  if (direccion) {
    url = `../clima/${direccion}/`;
  } else {
    url = `../clima/${latitud}_${longitud}_son_coordenadas/`;
  }

  fetch(url)
    .then((response) => response.json())
    .then((element) => {
      let temperatura = `${element['temp']}°C`;
      let descripcion = element['weather']['description'];
      let recomendacion = element['recomendacion'];
      let icono = element['weather']['icon'];

      // CREAR AQUI LOS ELEMENTOS PARA AGREGAR A LA INFORMACION DEL CLIMA EN EL FRONT
      // DEJE ESTE LOG PARA QUE VEAS LO QUE MUESTRA, SI NECESITAS OTRA INFO AVISAME
      // CREE UNA CARPETA DENTRO DE STATIC CON LOS ICONOS DEL API DEL CLIMA
      // PUEDES ACCESAR A ELLOS CON LA RUTA LOCAL MAS LA VARIABLE icono QUE PUSE
      console.log(temperatura, descripcion, recomendacion, icono);
      document.getElementById('tiempo-img').setAttribute("src", "static/core/icons/" + icono + 
      ".png");
      clima.innerHTML =
      "<h4 class='display-4 letra-caja'>" +
      temperatura + 
      "</h4><h4 class='display-4 letra-caja-info'>" +
      descripcion + 
      "</h4><h4 class='display-4 letra-caja-info'>" +
      recomendacion +
      '</h4>';
    });
}

// FUNCION PARA OBTENER INFORMACION DE FASE
// NOTA: SI SE DESEA CARGAR LA FUNCION CON DIRECCION SE DEBE LLAMAR DE LA SIGUIENTE MANERA:
// fetchFase(undefined, undefined, direccion)
function fetchFase(latitud, longitud, direccion = false) {
  var fase = document.getElementById('fase');
  let url;
  if (direccion) {
    url = `../covid/${direccion}/`;
  } else {
    url = `../covid/${latitud}_${longitud}_son_coordenadas/`;
  }

  fetch(url)
    .then((response) => response.json())
    .then((element) => {
      comuna = element['comuna'];
      numero_fase = element['numero_fase'];
      nombre_fase = element['nombre_fase'];

      // CREAR AQUI LOS ELEMENTOS PARA AGREGAR A LA INFORMACION DEL CLIMA EN EL FRONT
      // DEJE ESTE LOG PARA QUE VEAS LO QUE MUESTRA
      console.log(comuna, numero_fase, nombre_fase);
      fase.innerHTML =
      "<h4 class='display-4 letra-caja'>" +
      comuna + 
      ", Se encuentra en fase " +
      numero_fase + 
      " (" +
      nombre_fase +
      ')</h4>';
    });
}
