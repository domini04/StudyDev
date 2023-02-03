"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include #include : a function that allows referencing other URLconfs
from django.urls import path #path : a function that is used to map URLs to views
from polls import views #views : a Python module that contains the functions that will be called when a URL is matched

#urlpatterns : a list of URL patterns that Django will try to match the requested URL to find the correct view
    #if the requested URL matches a pattern, Django will execute the specified view and pass an HttpRequest object as the first argument to the view function
urlpatterns = [
    path('', views.home, name='home'), #'' : the empty string matches the base URL
    path('admin/', admin.site.urls), #admin/ : the URL that will be matched
    path('polls/', include('polls.urls')) #by using include(), we can reference other URLconfs
]

