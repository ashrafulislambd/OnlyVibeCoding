from django.urls import path

from . import views

urlpatterns = [
    path('inbox', views.LatestMessagesView.as_view(), name="inbox"),
]