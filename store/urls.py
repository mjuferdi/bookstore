from django.conf.urls import url
from . import views

# OPEN TEMPLATE IN VIEWS
urlpatterns = [
    url(r'^$', views.store, name='index'),
]