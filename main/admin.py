from django.contrib import admin
from .models import ToDoList, ItemToDo
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(ItemToDo)