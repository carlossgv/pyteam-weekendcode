from django.urls import path
from . import views

urlpatterns = [
    path("clima/", views.HomeView.as_view(), name="clima"),
    path(
        "clima/<usuario_latitud>/<usuario_longitud>/",
        views.devolver_clima,
        name="devolver_clima",
    ),
    path("clima/<direccion>/", views.clima_direccion, name="clima_direccion"),
]