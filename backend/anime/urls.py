from . import views
from urllib import request
from django.urls import path

urlpatterns = [
    path('', views.general),
    path('<str:animeName>', views.name),
]
