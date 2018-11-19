from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^pensum/nuevo/$', views.pensum_nuevo, name='pensum_nuevo'),
    ]
