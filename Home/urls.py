from .views import createModels, base2, addModelEntries, showObjectLists
from django.contrib import admin
from django.urls import path,include
from Home import views
admin.site.site_header = "TableApp admin"
admin.site.site_title = "TableApp admin"
admin.site.index_title = "Welcome to TableApp Admin"
urlpatterns = [
  path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('',include('social_django.urls')),
    path('logout/', views.logout, name='logout'),
    path('createModels', createModels, name='create_models'),
    path('addModelEntries', addModelEntries, name='add_entries'),
    path('showObjectLists', showObjectLists, name='show_objects'),
    path('baseApp/', base2, name='base_app'),
]
