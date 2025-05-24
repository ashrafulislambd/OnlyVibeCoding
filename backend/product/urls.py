from django.urls import path
from . import views

urlpatterns = [
    path('new', views.CreateView.as_view(), name="create_product")
]