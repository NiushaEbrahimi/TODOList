from django.shortcuts import render, get_object_or_404, redirect
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
    success_url = '/'
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['items'] = ItemToDo.objects.filter(todolist=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        item_id = request.POST.get("item_id")
        if item_id:
            item = get_object_or_404(ItemToDo, id=item_id, todolist=self.object)
            item.is_completed = not item.is_completed
            item.save()
        return redirect("todolist_detail", pk=self.object.pk)

class ToDoDetailCreate(CreateView):
    model = ToDoList
    template_name = 'main/todolist_detail.html'
    context_object_name = 'lists'
    queryset = ToDoList.objects.all()
    fields = ['title']
    success_url = '/'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

def home_view(request, *args, **kwargs):
    return render(request, 'main/home.html', {})