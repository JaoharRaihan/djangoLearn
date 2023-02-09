from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contract",views.contract,name='contract'),
    path("Photos",views.Photos,name='Photos'),


    
]