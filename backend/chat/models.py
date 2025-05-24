from django.db import models
from django.contrib.auth.models import User

class InboxMessage(models.Model):
    message = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.message[:20]