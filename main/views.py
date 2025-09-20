from django.shortcuts import render
from .models import ToDoList, ItemToDo
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.
class ToDoListView(ListView):
    model = ToDoList 
    template_name = 'main/todolist_list.html'
    queryset = ToDoList.objects.all()
    context_object_name = 'lists' 
    # print(queryset)
    # def get_absolute_url(self):
    #     return reverse('main:home')
    
class ToDoDetailView(DetailView):
    model = ToDoList
    template_name = 'main/todolist_detail.html'
    context_object_name = 'lists'
    queryset = ToDoList.objects.all()
    # queryset2 = ItemToDo.objects.all()

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['items'] = ItemToDo.objects.filter(todolist=self.object)
        return context
    
def home_view(request, *args, **kwargs):
    return render(request, 'main/home.html', {})