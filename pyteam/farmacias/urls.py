from django.urls import path
from . import views

urlpatterns = [
    path('test_farmacias/', views.TestView.as_view(), name="test"),
    path('farmacias/', views.encuentra_farmacias_cercanas, name="farmacias"),
]