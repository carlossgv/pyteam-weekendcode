import requests
from requests.exceptions import HTTPError

url = "https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos"


# Solicita la API y devuelve el JSON
def cargar_api(url):
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


data = cargar_api(url)
datos_farmacia(data, "245")
