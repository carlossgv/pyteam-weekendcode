from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class TestView(TemplateView):
    template_name = "farmacias/test.html"