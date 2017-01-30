from django.contrib import admin
from .models import Book, Author

# SHOW DATA IN DATABASE IN ADMIN


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)