from django.urls import path
from . import views

urlpatterns = [
    path('', views.fortune, name='fortune'), #path() : function that takes 3 arguments: route, view, and name
]
