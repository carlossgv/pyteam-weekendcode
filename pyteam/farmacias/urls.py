from django.urls import path
from . import views

urlpatterns = [
    path('farmacias/', views.TestView.as_view(), name="test"),
]