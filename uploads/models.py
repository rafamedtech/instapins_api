from django.db import models
from users.models import UserProfile
import uuid


# Image directory path
def user_directory_path(instance, filename):
    return 'uploads/{0}'.format(instance.user, filename)
    # return 'uploads/{0}/{1}'.format(instance.id, filename)


class Upload(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image = models.ImageField(blank=True, null=True)
    # image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

