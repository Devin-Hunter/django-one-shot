from django.urls import path
from todos.views import todolist_list

urlpatterns = [
    path("", todolist_list, name="todolist_list"),
]
