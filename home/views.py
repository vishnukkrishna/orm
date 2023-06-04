from django.shortcuts import render
from .models import Book, Users
# Create your views here.


def home(request):
    # post = Book.objects.all()
    
    # print(connection.quries)
    post = Book.objects.raw("select * from home_Book")
    print(post)
    return render(request, 'output.html', {'post': post})