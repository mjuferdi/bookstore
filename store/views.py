from django.shortcuts import render
from .models import Book

# RENDER TEMPLATE


def index(request):
    return render(request, 'template.html')


def store(request):
    # GETTING DATA FROM DATABASE
    count = Book.objects.all().count()
    context = {
        'count' : count,
    }
    request.session['location'] = "unknown"
    if request.user.is_authenticated():
        request.session['location'] = "Earth"
    return render(request, 'base.html', context)
