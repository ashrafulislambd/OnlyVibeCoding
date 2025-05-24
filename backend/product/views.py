from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Product

class CreateProduct(CreateView):
    model = Product
    template_name = 'core/edit_profile.html'
    success_url = '/'

    def get_object(self, queryset = None):
        return None
