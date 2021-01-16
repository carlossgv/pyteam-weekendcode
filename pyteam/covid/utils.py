import requests
from unidecode import unidecode
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


# Funcion que indica el numero de fase y nombre de la fase basado en la comuna indicada como parametro
def fase_comuna(comuna):
    url_cuarentena = (
        "https://atlas.jifo.co/api/connectors/4a473aa1-701e-4c04-acd2-b425056f5c03"
    )

    data = cargar_api(url_cuarentena)["data"][0]

    for item in data:
        if unidecode(item[0].lower()) == unidecode(comuna.lower()):
            datos_comuna = {
                "comuna": item[0],
                "numero_fase": item[1],
                "nombre_fase": item[2],
            }
            break
        else:
            datos_comuna = "No hay información disponible de la comuna"

    return datos_comuna
