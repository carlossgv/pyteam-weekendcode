from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, Http404
from pyteam.utils import devuelve_datos_usuario, devuelve_latlng_usuario
import os

# Create your views here.
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {"key_google": os.environ.get("KEY_GOOGLEMAPS")},
        )


def encuentra_datos_usuario(request, direccion):
    if "son_coordenadas" in direccion:
        direccion = direccion.split("_")
        usuario_latitud = float(direccion[0])
        usuario_longitud = float(direccion[1])
    else:
        usuario_latitud, usuario_longitud = devuelve_latlng_usuario(direccion)

    # if usuario_latitud == None or usuario_longitud == None:
    #     raise Http404(
    #         "Algo ha fallado con respecto a la latitud o longitud de la ubicacion del usuario"
    #     )

    datos_usuario = devuelve_datos_usuario(usuario_latitud, usuario_longitud)

    if datos_usuario:
        return JsonResponse(datos_usuario)
    else:
        return JsonResponse({"local_id": "-1"})  # En caso de no haber datos de usuario
