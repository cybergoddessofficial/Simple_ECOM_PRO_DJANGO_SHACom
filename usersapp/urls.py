
from django.urls import path

import usersapp
from usersapp import views

urlpatterns = [

    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('discat/<itemcatname>',views.discat,name="discat"),
    path('singlepro/<sp>',views.singlepro,name="singlepro"),
    path('registeruser',views.registeruser,name="registeruser"),
    path('loginuser',views.loginuser,name="loginuser")
]
