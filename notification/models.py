from django.db import models

from django.conf import settings



# Create your models here.
class Notification(models.Model):
    CHANNEL_TYPE = (
        ('EMAIL', 'Email'),
        ('SMS', 'SMS'),
        ('WEBHOOK', 'Webhook'),
    )
    wallet = models.CharField(max_length=10, null=True, blank=True)
    reference_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    channel = models.CharField(max_length=10, choices=CHANNEL_TYPE, default='EMAIL')
    event_type = models.CharField(max_length=30)
    is_read = models.BooleanField(default=False)
