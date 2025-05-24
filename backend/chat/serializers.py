from rest_framework import serializers
from django.contrib.auth.models import User
from .models import InboxMessage

class InboxMessageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = InboxMessage
        fields = ['id', 'message', 'user', 'sender', 'timestamp', 'image']
        read_only_fields = ['id', 'sender', 'timestamp']

    def create(self, validated_data):
        # Automatically set the sender from the request context
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)
