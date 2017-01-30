from django.conf.urls import url
from . import views

# OPEN TEMPLATE IN VIEWS
urlpatterns = [
    url(r'^$', views.store, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
]