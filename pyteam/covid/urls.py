from django.urls import path
from . import views

urlpatterns = [
    path("covid/", views.HomeView.as_view(), name="covid"),
    path("covid/<direccion>/", views.info_cuarentena, name="info_cuarentena"),
]