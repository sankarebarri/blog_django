from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_detail = models.CharField(max_length=1000, blank=True)
    user_image = models.ImageField(default='user_image_default.jpg', upload_to='user_profile_image')


    def __str__(self):
        return f'{self.name.username} Profile'
