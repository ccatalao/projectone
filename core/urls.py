from django.urls import path
from . import views


urlpatterns = [
    #path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.post_list_view, name="post_list")


]