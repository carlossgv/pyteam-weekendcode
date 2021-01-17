from django.urls import path
from . import views

urlpatterns = [
    path("clima/", views.HomeView.as_view(), name="clima"),
    path("clima/<direccion>/", views.devolver_clima, name="devolver_clima"),
]