from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoItem

# Create your views here.
def todolist_list(request):
    todolist = TodoList.objects.all()
    context = {
        "todolist": todolist,
    }
    return render(request, "todos/list.html", context)
