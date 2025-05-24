from rest_framework import serializers
from .models import InboxMessage

class InboxMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InboxMessage
        fields = ['id', 'message', 'user', 'timestamp', 'image']
