from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from .utils import devuelve_farmacias_cercanas

# Create your views here.

class TestView(TemplateView):
    template_name = "farmacias/test.html"

def encuentra_farmacias_cercanas(request, usuario_latitud = -32.878131, usuario_longitud = -71.244828):

    url = "https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos"
    
    farmacias_cercanas = devuelve_farmacias_cercanas(usuario_latitud, usuario_longitud, url)
    #print(farmacias_cercanas)
    json_response = []
    if farmacias_cercanas:
        for farmacia in farmacias_cercanas:
            json_response.append({
                'id': farmacia['local_id'],
                'latitud':farmacia['local_lat'], 
                'longitud':farmacia['local_lng'], 
                'nombre':farmacia['local_nombre']
                })
    else:
        return JsonResponse([{'id':'-1'}], safe=False) # En caso de no haber farmacias cercanas devuelve esto
    return JsonResponse(json_response, safe=False)