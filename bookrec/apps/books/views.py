from django.shortcuts import render
from django.views import generic
from .models import Book
from django.conf import settings
# Create your views here.

def IndexView(request):
    books = Book.objects.all()
    print(len(books))
    context = {'books':books}
    return render(request, 'index.html',context)

def DetailView(request,id):
    book = Book.objects.get(id=id)
    context = {'book':book}
    return render(request,'detail.html',context)