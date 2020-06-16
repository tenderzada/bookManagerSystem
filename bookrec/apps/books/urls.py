# posts/urls.py
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('books/',views.IndexView,name='bookslist'),  # 主页，自然排序
    path('booksdetail/<int:id>/',views.DetailView,name ='booksdetail')
    ]
