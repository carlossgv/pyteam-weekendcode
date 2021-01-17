from .utils import info_clima
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, Http404
from googletrans import Translator
from pyteam.utils import devuelve_latlng_usuario


# Create your views here.
class HomeView(TemplateView):
    template_name = "clima/home.html"


def devolver_clima(request, direccion):
    if "son_coordenadas" in direccion:
        direccion = direccion.split("_")
        usuario_latitud = float(direccion[0])
        usuario_longitud = float(direccion[1])
    else:
        usuario_latitud, usuario_longitud = devuelve_latlng_usuario(direccion)
    
    datos_clima = info_clima(usuario_latitud, usuario_longitud)
    print ("***********", datos_clima)
    # traducir descripcion a espanol
    descripcion = datos_clima["weather"]["description"]

    translator = Translator(service_urls=["translate.googleapis.com"])
    descripcion = translator.translate(descripcion, dest="es").text
    datos_clima["weather"]["description"] = descripcion

    if datos_clima:
        return JsonResponse(datos_clima, safe=False)
    else:
        return JsonResponse([{"datos_clima": "no encontrado"}], safe=False)