from django.db import models
from users.models import UserProfile
import uuid

# Create your models here.

class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # pin = models.ForeignKey(Pin, on_delete=models.CASCADE)

class Pin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    label = models.CharField(max_length=250)
    url = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250)
    owner = models.ForeignKey(UserProfile, related_name='pins', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comments, related_name='pins', blank=True)

    def __str__(self):
        return self.label