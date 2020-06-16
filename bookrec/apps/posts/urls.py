# posts/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('postsdetail/<int:pk>/', views.PostDetail.as_view()),]
