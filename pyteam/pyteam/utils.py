import requests
from requests.exceptions import HTTPError

from geopy import distance
from geopy import geocoders

AGENT_NOMINATIM = "Py_Team"


def cargar_api(url: str, headers: dict = False) -> list:
    """
    Cargamos todo el contenido de la api de farmacias de turnos,
    si tiene headers también se le pueden agregar como parametros

    Returns
    -------
    data: list
        Una lista de diccionarios, donde cada diccionario contiene la informacion de una farmacia

    """
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


def devuelve_latlng_usuario(direccion: str) -> tuple:
    """
    Encuentra la latitud y longitud para una direccion dada

    Returns
    -------
    location: tuple
        Una tupla con floats con la latitud y longitud,
        en caso de no encontrar la direccion devuelve una tupla con Nones

    """

    geolocator = geocoders.Nominatim(user_agent=AGENT_NOMINATIM)

    location = geolocator.geocode(direccion)

    if location == None:
        return (None, None)

    return (location.latitude, location.longitude)


def devuelve_comuna(latitud: float, longitud: float) -> str:
    """
    Encuentra la comuna del usuario

    Parameters
    ----------
    latitud: float
        En principio espera un float pero puede ser un str tambien
    longitud: float
        En principio espera un float pero puede ser un str tambien

    Returns
    -------
    comuna: str
        un string con la comuna del usuario,
        en caso de no encontrar la direccion devuelve un string vacio

    """
    geolocator = geocoders.Nominatim(user_agent=AGENT_NOMINATIM)

    location = geolocator.reverse(f"{latitud}, {longitud}")

    if location == None:
        return ""

    comuna = location.raw["address"].get("city")

    if comuna == None:
        comuna = "Comuna no encontrada"

    return comuna


def devuelve_datos_usuario(latitud: float, longitud: float) -> dict:
    """
    Devuelve los datos generales del usuario

    Parameters
    ----------
    latitud: float
        En principio espera un float pero puede ser un str tambien
    longitud: float
        En principio espera un float pero puede ser un str tambien

    Returns
    -------
    datos_usuario: dict
        un diccionario con los datos del usuario
        en caso de no encontrar la direccion devuelve un diccionario vacio

    """

    geolocator = geocoders.Nominatim(user_agent=AGENT_NOMINATIM)

    location = geolocator.reverse(f"{latitud}, {longitud}")

    if location == None:
        return {}

    direccion = location.raw["address"].get("road")
    numero = location.raw["address"].get(
        "house_number"
    )  # Este es con get porque si no existe devuelve None
    comuna = location.raw["address"].get("city")
    region = location.raw["address"].get("state")

    datos_usuario = {
        "direccion": direccion,
        "numero": numero,
        "comuna": comuna,
        "region": region,
    }

    return datos_usuario