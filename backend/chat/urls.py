from django.urls import path

from . import views

urlpatterns = [
    path('<int:other_user>', views.inbox_view, name="inbox_ui"),
    path('inbox', views.LatestMessagesView.as_view(), name="inbox"),
    path('send-message', views.SendMessageView.as_view(), name="send_message"),
]