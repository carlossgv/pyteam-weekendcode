def coordenadas_totales(data):

    coordenadas = []

    for farmacia in data:
        coordenada = {
            "local_id": farmacia["local_id"],
            "local_lat": farmacia["local_lat"],
            "local_lng": farmacia["local_lng"],
        }

        coordenadas.append(coordenada)

        print(coordenada)

    return coordenadas