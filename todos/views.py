from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoItem

# Create your views here.
def todo_list_list(request):
    todolist = TodoList.objects.all()
    context = {
        "todolist": todolist,
    }
    return render(request, "todos/list.html", context)

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/detail.html", context)
