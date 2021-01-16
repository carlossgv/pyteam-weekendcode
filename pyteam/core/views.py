from django.views.generic.base import TemplateView
from django.shortcuts import render
import os

# Create your views here.
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'key_google':os.environ.get("KEY_GOOGLEMAPS")})