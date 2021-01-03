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


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task
    }
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('taskList')
    return render(request, 'task/update_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('taskList')

    context = {'task': task}
    return render(request, 'task/delete_task.html',
                  context)
