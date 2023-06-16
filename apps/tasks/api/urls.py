from django.urls import path
from .api_views import user_task_api_view

urlspatterns = [
    path('tasks/user/<int:user_id>', user_task_api_view, name='user_task_api_view')
]
