from django.urls import path
from .views import ToDoListView, ToDoDetailView, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('Lists/', ToDoListView.as_view(), name='Lists'),
    path('Lists/<int:pk>/', ToDoDetailView.as_view(), name='ListDetail'),

]