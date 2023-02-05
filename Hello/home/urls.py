from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("Photos",views.Photos,name='Photos'),
    path("contract",views.contract,name='contract'),


    
]