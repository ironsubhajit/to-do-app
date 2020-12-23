from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskListView.as_view(), name='taskList'),
    path('task_update/<int:pk>/', update_task, name='update_task')
]