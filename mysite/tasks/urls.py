from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('detail/<int:pk>/', views.TasksDetailView.as_view(), name='detail'),
    path("", views.TasksIndexView.as_view(), name="index"),
    path("create", views.TasksCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.TasksUpdateView.as_view(), name="update"),
    path("task-delete/<int:pk>/", views.TasksDeleteView.as_view(), name="task-delete"),
    path("mark-complete/<int:task_id>/", views.mark_complete, name="mark-complete"),
    path("undo/<int:task_id>/", views.undo, name="undo")
    ]
