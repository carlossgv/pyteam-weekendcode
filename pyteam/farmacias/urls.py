from django.urls import path
from . import views

urlpatterns = [
    path('test_farmacias/', views.TestView.as_view(), name="test"),
    path('farmacias/<usuario_latitud>/<usuario_longitud>/', views.encuentra_farmacias_cercanas, name="farmacias"),
    path('farmacias/direccion/', views.encuentra_farmacias_by_direccion, name="farmacias_direccion"),
]