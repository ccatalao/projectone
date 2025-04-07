from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='flickr_album_list'),
    path('album/<str:album_id>/', views.album_detail, name='flickr_album_detail'),
] 