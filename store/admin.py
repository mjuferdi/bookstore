from django.contrib import admin
from .models import Book

# SHOW DATA IN DATABASE IN ADMIN
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')

admin.site.register(Book, BookAdmin)