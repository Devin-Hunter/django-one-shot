from django.forms import ModelForm
from todos.models import TodoList

class CreateForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["name"]
