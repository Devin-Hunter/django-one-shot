from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoItem
from todos.forms import CreateForm, CreateItemForm

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

def todo_list_update(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = CreateForm(instance=todo_list)
    context = {
        "form": form,
        "todo_list": todo_list
    }
    return render(request, "todos/update.html", context)

def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        todo_list.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")

def todo_item_create(request):
    if request.method == "POST":
        form = CreateItemForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            return redirect("todo_list_detail", id=new_item.list.id)
    else:
        form=CreateItemForm()
    context = {
        "form": form,
    }
    return render(request, "items/create.html", context)

def todo_item_update(request, id):
    todo_item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = CreateItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            todo_item = form.save()
            return redirect("todo_list_detail", id=todo_item.list.id)
    else:
        form = CreateItemForm(instance=todo_item)
    context = {
        "form": form,
        "todo_item": todo_item
    }
    return render(request, "items/edit.html", context)
