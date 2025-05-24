from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import InboxMessage
from .serializers import InboxMessageSerializer

class LatestMessagesView(ListAPIView):
    serializer_class = InboxMessageSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    def get_queryset(self):
        incoming = InboxMessage.objects.filter(user=self.request.user)
        outgoing = InboxMessage.objects.filter(sender=self.request.user)
        return incoming.union(outgoing).order_by('-timestamp')[:20]
    
def inbox_view(request, other_user):
    context = {
        'current_user_id': request.user.id,
        'other_user_id': int(other_user),
        'inbox_url': "{% url 'inbox' %}"
    }
    return render(request, 'chat/chatui.html', context)

class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = InboxMessageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            message = serializer.save()
            return Response({'success': True, 'message_id': message.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
