from django.test import TestCase
from geopy import distance
from geopy import geocoders

# Create your tests here.
class DistanceTestCase(TestCase):
    def setUp(self):
        self.farmacias = [
            {'latitud':-32.9851431062104, 'longitud':-71.2763421550883, 'comuna':'Limache', 'nombre': 'Salcobrand'},
            {'latitud':-32.8252324978247, 'longitud':-71.2268391982971, 'comuna':'La cruz', 'nombre': 'La Cruz'},
            {'latitud':-32.8777193144105, 'longitud':-71.2453034649053, 'comuna':'Quillota', 'nombre': 'Italia'}
        ]

        self.ubicacion_usuario =  {'latitud':-32.878131, 'longitud':-71.244828, 'comuna':'Quillota'}

    def test_comprobar_farmacias_cercanas(self):

        farmacias_cercanas = []

        coordenada_usuario = (self.ubicacion_usuario['latitud'], self.ubicacion_usuario['longitud'])
        
        for farmacia in self.farmacias:
            
            coordenada_farmacia = (farmacia['latitud'], farmacia['longitud'])
            if distance.distance(coordenada_farmacia, coordenada_usuario).km <= 5.0:
                farmacias_cercanas.append(farmacia)

        self.assertEqual(farmacias_cercanas[0]['nombre'], 'Italia')

class GeoTestcase(TestCase):
    def setUp(self):
        self.direccion = "Premio Nobel 3554" #"Av Carlos Valdovinos 62, San Joaquín, Región Metropolitana"
    def test_encontrar_comuna(self):
        geolocator = geocoders.Nominatim(user_agent="Py_Team")

        location1 = geolocator.geocode(self.direccion)
        
        print(location1.address)
        print((location1.latitude, location1.longitude))
        print(location1.raw)

        location2 = geolocator.reverse("-33.4723444, -70.5965725")
        
        print(location2.address)
        print((location2.latitude, location2.longitude))
        raw = location2.raw
        print(raw['address']['city'])

        self.assertEqual(raw['address']['city'], "Ñuñoa")
        

