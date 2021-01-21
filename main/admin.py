from django.contrib import admin
from .models import todo
# Register your models here.

admin.site.register(todo)

from .models import book
admin.site.register(book)