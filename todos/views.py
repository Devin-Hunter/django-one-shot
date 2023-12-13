from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoItem
from todos.forms import CreateForm

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

def todo_list_create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            new_list = form.save()
            return redirect("todo_list_detail", id=new_list.id)
    else:
        form=CreateForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create.html", context)
