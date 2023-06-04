from django.shortcuts import render
from .models import Book, Users
from django.db import connection
# Create your views here.


def home(request):
    # post = Book.objects.all()
    
    
    post = Book.objects.raw("select * from home_Book")
    print(post)
    cursor = connection.cursor()
    cursor.execute("select * from home_Book")
    r = cursor.fetchone()
    print(r)
    print(connection.queries)
    return render(request, 'output.html', {'post': post})