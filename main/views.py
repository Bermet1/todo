from django.shortcuts import render, HttpResponse
from .models import todo
from .models import book
# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def third(request):
    book_list = book.objects.all()
    return render(request, "This is page test3", {"book": book})
