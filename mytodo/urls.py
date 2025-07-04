from django.urls import path
from mytodo import views as mytodo
from . import views
from .views import TaskUpdateView


urlpatterns = [
    path("", mytodo.index,name="index"),
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
    path("add/", mytodo.add,name="add"),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name="task_update"),
    path('<int:pk>/delete/', mytodo.task_delete, name='task_delete'),
]