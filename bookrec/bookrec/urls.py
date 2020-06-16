"""bookrec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path,include
from django.conf.urls import url

from rest_framework import routers
from api import views as api_views

from books import views as books_views

router = routers.DefaultRouter()
router.register(r'posts', api_views.PostListSet)
# router.register(r'postsdetail', api_views.PostDetail)
router.register(r'books', api_views.BookListSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('books.urls'))
]
urlpatterns.append(url(r'^api/v1/', include(router.urls)))