from django.db import models
import uuid

# Image directory path
def user_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.id, filename)

class Upload(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

