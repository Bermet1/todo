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

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form ["book_description"]
    price = form ["book_price"]
    genre = form ["book_genre"]
    author = form["book_author"]
    year = form ["book_year"]
    Book = book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    Book.save()
    return redirect(third)

def delete_todo(request, id):
    ToDo = todo.objects.get(id=id)
    ToDo.delete()
    return redirect(test)

def mark_todo(request, id):
    ToDo = todo.objects.get(id=id)
    ToDo.is_favorite = True
    ToDo.save()
    return redirect(test)

def unmark_todo(request, id):
    ToDo = todo.objects.get(id=id)
    ToDo.is_favorite = False
    ToDo.save()
    return redirect(test)

def done_todo(request, id):
    ToDo = todo.objects.get(id=id)
    ToDo.is_closed = not ToDo.is_closed
    ToDo.save()
    return redirect(test)

