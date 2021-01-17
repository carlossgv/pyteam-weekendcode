from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import JsonResponse, Http404
from .utils import devuelve_farmacias_cercanas
from pyteam.utils import devuelve_latlng_usuario

URL = "https://farmanet.minsal.cl/maps/index.php/ws/getLocalesTurnos"

# Create your views here.

class TestView(TemplateView):
    template_name = "farmacias/test.html"

def encuentra_farmacias_cercanas(request, usuario_latitud = None, usuario_longitud = None):

    if usuario_latitud == None or usuario_longitud == None:
        raise Http404("Algo ha fallado con respecto a la latitud o longitud de la ubicacion del usuario")

    usuario_latitud = float(usuario_latitud)
    usuario_longitud = float(usuario_longitud)
    
    farmacias_cercanas = devuelve_farmacias_cercanas(usuario_latitud, usuario_longitud, URL)
    
    if farmacias_cercanas:
        return JsonResponse(farmacias_cercanas, safe=False)        
    else:
        return JsonResponse([{'local_id':'-1'}], safe=False) # En caso de no haber farmacias cercanas devuelve esto

    # return JsonResponse(farmacias_cercanas, safe=False)

def encuentra_farmacias_by_direccion(request):

    direccion = request.GET.get('direccion')

    if direccion:
        
        usuario_latitud, usuario_longitud = devuelve_latlng_usuario(direccion)

        # En caso de que la direccion no haya sido encontrada devuelve lo siguiente
        if usuario_latitud == None:
            return JsonResponse([{'local_id':'-2'}], safe=False) 

        farmacias_cercanas = devuelve_farmacias_cercanas(usuario_latitud, usuario_longitud, URL)

        if farmacias_cercanas:
            return JsonResponse(farmacias_cercanas, safe=False)        
        else:
            return JsonResponse([{'local_id':'-1'}], safe=False)
        
    else:
        return JsonResponse([{'local_id':'-2'}], safe=False)

    