from django.shortcuts import render
from .models import Book

# RENDER TEMPLATE


def index(request):
    return render(request, 'template.html')


def store(request):
    # GETTING DATA FROM DATABASE
    books = Book.objects.all()
    context = {
        'books' : books,
    }
    return render(request, 'base.html', context)


def book_details(request, book_id):
    context = {
        'book' : Book.objects.get(pk=book_id)
    }
    return render(request, 'store/detail.html', context)
