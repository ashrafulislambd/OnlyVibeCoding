from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Product, Category
from core.models import Profile

class CreateProduct(CreateView, LoginRequiredMixin):
    model = Product
    fields = ['name', 'description', 'image', 'listing_type', 'pricing_type',
            'visibility', 'category', 'price', 'starting_bid']
    template_name = 'product/new_product.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AllListing(ListView, LoginRequiredMixin):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["universities"] = Profile.objects.values_list("university", flat=True).distinct()
        context["categories"] = Category.objects.values_list("name", flat=True).distinct()
        return context

    def get_queryset(self):
        own_uni = Product.objects.filter(user__profile__university=self.request.user.profile.university,
                                        visibility='private')
        public = Product.objects.filter(visibility='public')
        if 'search-input' in self.request.GET:
            own_uni = own_uni.filter(name__icontains=self.request.GET['search-input'])
            public = public.filter(name__icontains=self.request.GET['search-input'])
        if 'min-price' in self.request.GET and self.request.GET['min-price'] != "":
            sminp = self.request.GET['min-price']
            if sminp == "":
                min_price = 0
            else:
                min_price = float(sminp)
            own_uni = own_uni.filter(price__gte=min_price)
            public = public.filter(price__gte=min_price)
        if 'max-price' in self.request.GET and self.request.GET['max-price'] != "":
            smaxp = self.request.GET['max-price']
            if smaxp == "":
                max_price = 0
            else:
                max_price = float(smaxp)
            own_uni = own_uni.filter(price__lte=max_price)
            public = public.filter(price__lte=max_price)
        if 'category' in self.request.GET and self.request.GET['category'] != "all":
            own_uni = own_uni.filter(category__name=self.request.GET['category'])
            public = public.filter(category__name=self.request.GET['category'])
        if 'university' in self.request.GET and self.request.GET['university'] != "all":
            own_uni = own_uni.filter(user__profile__university=self.request.GET['university'])
            public = public.filter(user__profile__university=self.request.GET['university'])
        
        all = own_uni.union(public)
        return all