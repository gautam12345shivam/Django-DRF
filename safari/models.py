from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=20, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username



