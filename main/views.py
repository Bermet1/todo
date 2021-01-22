from django.shortcuts import render, HttpResponse, redirect
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
    return render(request, "books.html", {"book_list": book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    ToDo = todo(text=text)
    ToDo.save()
    return redirect(test)