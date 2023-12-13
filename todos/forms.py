from django.forms import ModelForm
from todos.models import TodoList, TodoItem

class CreateForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["name"]

class CreateItemForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "due_date",
            "is_completed",
            "list",
        ]
