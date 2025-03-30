from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields for user profile
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    is_seller = models.BooleanField(default=False)
    is_renter = models.BooleanField(default=False)

    def __str__(self):
        return self.username