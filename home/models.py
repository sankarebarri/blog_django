from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

class BlogDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    #content_image = models.ImageField()

    def __str__(self):
        return self.title
