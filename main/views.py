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
    
class ToDoDetailView(DetailView):
    model = ToDoList
    template_name = 'main/todolist_detail.html'
    context_object_name = 'lists'
    queryset = ToDoList.objects.all()
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
    template_name = 'main/todolist_create.html'
    context_object_name = 'lists'
    queryset = ToDoList.objects.all()
    fields = ['title']
    success_url = '/'

    def form_valid(self, form):
        todolist = form.save()
        item_titles = self.request.POST.getlist("item_title[]")
        item_end_dates = self.request.POST.getlist("item_end_date[]")

        for title, end_date in zip(item_titles, item_end_dates):
            ItemToDo.objects.create(
                todolist=todolist,
                title=title,
                end_date=end_date if end_date else None
            )
        return redirect("Lists")
    
class ToDoDetailEdit(UpdateView):
    model = ToDoList
    template_name = 'main/todolist_edit.html'
    context_object_name = 'lists'
    queryset = ToDoList.objects.all()
    fields = ['title', 'ended_at']
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if "delete" in request.POST:
            self.object.delete()
            return redirect(self.success_url)

        return super().post(request, *args, **kwargs)
    

def home_view(request, *args, **kwargs):
    return render(request, 'main/home.html', {})