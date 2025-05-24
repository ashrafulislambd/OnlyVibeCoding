from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllListing.as_view(), name="product_listing"),
    path('new', views.CreateProduct.as_view(), name="create_product")
]