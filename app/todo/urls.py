from django.urls import path
from .views import CompletedTasksView, TasksView

urlpatterns = [
    path('todo', TasksView.as_view()),
    path('todo/<str:pk>', TasksView.as_view()), # to capture our ids
    path('done', CompletedTasksView.as_view()), # for completed todos
]
