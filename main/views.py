from django.shortcuts import render, HttpResponse
from .models import todo
# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def third(request):
    return HttpResponse("This is page test3")
