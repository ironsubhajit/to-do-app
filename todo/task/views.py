from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import TaskForm
from .models import *


class TaskListView(ListView):
    model = Task
    paginate_by = 10

    context_object_name = 'tasks'
    template_name = 'task/index.html'

    def post(self, request, *args, **kwargs):
        self.form = TaskForm(self.request.POST or None)
        if self.form.is_valid():
            self.form.save()
            return redirect('taskList')
        else:
            return super(TaskListView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

