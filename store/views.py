from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, 'template.html')


def store(request):
    # GETTING DATA FROM DATABASE
    count = Book.objects.all().count()
    context = {
        'count' : count,
    }
    return render(request, 'store.html', context)
