from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    user_detail = models.CharField(max_length=1000)


    def __str__(self):
        return f'{self.name.username} Profile'
