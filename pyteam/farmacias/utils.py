import requests
from geopy import distance
from requests.exceptions import HTTPError

# Solicita la API y devuelve el JSON
def cargar_api(url):
    """
    Cargamos todo el contenido de la api de farmacias de turnos

    Returns
    -------
    data: list
        Una lista de diccionarios, donde cada diccionario contiene la informacion de una farmacia
        
    """
    for url in [url]:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"Ocurrió un error HTTP: {http_err}")
        except Exception as err:
            print(f"Ocurrió otro error: {err}")
        else:
            print("API cargada")

    data = response.json()

    return data


# Devuelve las coordenadas de todas las farmacias para comparar con ubicación y conseguir las más cercanas
def coordenadas_totales(data):
    coordenadas = []

    for farmacia in data:
        coordenada = {
            "local_id": farmacia["local_id"],
            "local_lat": farmacia["local_lat"],
            "local_lng": farmacia["local_lng"],
        }

        coordenadas.append(coordenada)

    return coordenadas


# Devuelve todos los datos de una farmacia en especifico
def datos_farmacia(data, id_farmacia):
    for farmacia in data:
        if id_farmacia == farmacia["local_id"]:
            datos_farmacia = farmacia

    return datos_farmacia

def devuelve_farmacias_cercanas(usuario_latitud, usuario_longitud, url):
    """
    Buscamos las farmacias más cercanas al usuario, las cuales estamos considerando 
    son las que estan dentro de un rango de 5 km segun la distancia geodesica

    Returns
    -------
    farmacias_cercanas: list
        Una lista de diccionarios, donde cada diccionario contiene la informacion de una farmacia

    """

    farmacias = cargar_api(url)

    farmacias_cercanas = []

    coordenada_usuario = (usuario_latitud, usuario_longitud)

    for farmacia in farmacias:
        coordenada_farmacia = (farmacia["local_lat"], farmacia["local_lng"])
        if distance.distance(coordenada_farmacia, coordenada_usuario).km <= 5.0:
            farmacias_cercanas.append(farmacia)
    
    return farmacias_cercanas

# data = cargar_api(url)
# datos_farmacia(data, "245")
