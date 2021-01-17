from django.shortcuts import render
from django.views.generic.base import TemplateView
from .utils import fase_comuna
from django.http import JsonResponse, Http404
from pyteam.utils import devuelve_latlng_usuario, devuelve_comuna


# Create your views here.
class HomeView(TemplateView):
    template_name = "covid/home.html"


def info_cuarentena(request, direccion):
    if "son_coordenadas" in direccion:
        direccion = direccion.split("_")
        usuario_latitud = float(direccion[0])
        usuario_longitud = float(direccion[1])
    else:
        usuario_latitud, usuario_longitud = devuelve_latlng_usuario(direccion)

    comuna = devuelve_comuna(usuario_latitud, usuario_longitud)

    fase = fase_comuna(comuna)

    if fase_comuna:
        return JsonResponse(fase, safe=False)
    else:
        return JsonResponse([{"fase_comuna": "no encontrado"}], safe=False)
