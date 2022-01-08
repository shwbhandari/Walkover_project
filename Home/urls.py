from django.contrib import admin
from django.urls import path,include
from Home import views
urlpatterns = [
  path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('',include('social_django.urls')),
    path('logout/',views.logout,name='logout'),
]