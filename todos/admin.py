from django.contrib import admin
from todos.models import TodoList, TodoItem

# Register your models here.
@admin.register(TodoList)
class TodoList(admin.ModelAdmin):
    list_display = [
        "name",
        "id",
    ]

@admin.register(TodoItem)
class TodoItem(admin.ModelAdmin):
    list_display = [
        "task",
        "due_date",
    ]
