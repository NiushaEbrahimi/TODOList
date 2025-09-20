from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

class ItemToDo(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    end_date = models.DateTimeField(null=True, blank=True)