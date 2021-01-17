from .utils import info_clima
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, Http404
from googletrans import Translator
from pyteam.utils import devuelve_latlng_usuario


# Create your views here.
class HomeView(TemplateView):
    template_name = "clima/home.html"


def devolver_clima(request, usuario_latitud=None, usuario_longitud=None):
    if usuario_latitud == None or usuario_longitud == None:
        raise Http404(
            "Algo ha fallado con respecto a la latitud o longitud de la ubicacion del usuario"
        )

    usuario_latitud = float(usuario_latitud)
    usuario_longitud = float(usuario_longitud)

    datos_clima = info_clima(usuario_latitud, usuario_longitud)

    # traducir descripcion a espanol
    descripcion = datos_clima["weather"]["description"]

    translator = Translator(service_urls=["translate.googleapis.com"])
    descripcion = translator.translate(descripcion, dest="es").text
    datos_clima["weather"]["description"] = descripcion

    if datos_clima:
        return JsonResponse(datos_clima, safe=False)
    else:
        return JsonResponse([{"datos_clima": "no encontrado"}], safe=False)


def clima_direccion(request, direccion):

    print(f"entro a funcion clima con direccion {direccion}")

    if direccion:

        usuario_latitud, usuario_longitud = devuelve_latlng_usuario(direccion)

        print(direccion, usuario_latitud, usuario_longitud)
        # En caso de que la direccion no haya sido encontrada devuelve lo siguiente
        if usuario_latitud == None:
            return JsonResponse([{"local_id": "-2"}], safe=False)

        datos_clima = info_clima(usuario_latitud, usuario_longitud)

        # traducir descripcion a espanol
        descripcion = datos_clima["weather"]["description"]

        translator = Translator(service_urls=["translate.googleapis.com"])
        descripcion = translator.translate(descripcion, dest="es").text
        datos_clima["weather"]["description"] = descripcion

        if datos_clima:
            return JsonResponse(datos_clima, safe=False)
        else:
            return JsonResponse([{"datos_clima": "no encontrado"}], safe=False)
