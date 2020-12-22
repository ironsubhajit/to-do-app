from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class TaskListView(ListView):
    model = Task
    paginate_by = 10

    context_object_name = 'tasks'
    template_name = 'task/index.html'
