from django.shortcuts import render
from .models import BlogDetails
# Create your views here.
def home(request):

    context = {
        'posts': BlogDetails.objects.all()
    }

    return render(request, 'home/home.html', context)


def article(request, pk):
    article = BlogDetails.objects.get(id=pk)

    context = {
        'article': article
    }

    return render(request, 'home/article.html', context)
