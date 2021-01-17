from geopy import distance
from pyteam.utils import cargar_api

DISTANCIA_MINIMA = 5.0 # KM

def devuelve_farmacias_cercanas(usuario_latitud: float, usuario_longitud: float, url: str) -> list:
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

        check_latitud = farmacia["local_lat"].replace('.', '', 1).replace('-', '', 1)
        check_longitud = farmacia["local_lng"].replace('.', '', 1).replace('-', '', 1)

        # Checkeamos primero que la latitud y la longitud sea valida
        if check_latitud.isdigit() and check_longitud.isdigit():
        
            coordenada_farmacia =  (float(farmacia["local_lat"]), float(farmacia["local_lng"]))
            if distance.distance(coordenada_farmacia, coordenada_usuario).km <= DISTANCIA_MINIMA:
                farmacias_cercanas.append(farmacia)
    
    return farmacias_cercanas
