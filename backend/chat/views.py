from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import InboxMessage
from .serializers import InboxMessageSerializer

class LatestMessagesView(ListAPIView):
    serializer_class = InboxMessageSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def get_queryset(self):
        return InboxMessage.objects.filter(user=self.request.user).order_by('-timestamp')[:20]
