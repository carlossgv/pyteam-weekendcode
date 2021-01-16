import os
import requests
from requests.exceptions import HTTPError

# Cargar la api desde url indicado, si tiene headers también se le pueden agregar como parametros
# responde JSON con data
def cargar_api(url, headers=False):
    for url in [url]:
        try:
            if headers:
                response = requests.get(url, headers=headers)
            else:
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


WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
# funcion que da todos los datos del clima segun las coordenadas
# adicionalmente agrega un key "recomendacion" para alertar al usuario de precauciones a tomar antes de salir
# informacion de cada dato de la API: https://www.weatherbit.io/api/weather-current
# diferentes opciones de descripciones y logos aqui: https://www.weatherbit.io/api/codes
def info_clima(latitud, longitud):
    url_clima = f"https://api.weatherbit.io/v2.0/current?lat={latitud}&lon={longitud}&key={WEATHER_API_KEY}"

    info_clima = cargar_api(url_clima)["data"][0]

    descripcion_clima = info_clima["weather"]["description"]

    if (
        "Thunderstorm" in descripcion_clima
        or "Drizzle" in descripcion_clima
        or "Rain" in descripcion_clima
    ):
        info_clima["recomendacion"] = "¡Sal con paraguas! Lloverá"
    elif "snow" in descripcion_clima.lower():
        info_clima["recomendacion"] = "Cuidado en la vía, nevará"
    elif "Clear sky" in descripcion_clima:
        info_clima["recomendacion"] = "El día estará despejado hoy. ¡Protégete del sol!"
    else:
        info_clima["recomendacion"] = "¡Ten un excelente día!"

    return info_clima