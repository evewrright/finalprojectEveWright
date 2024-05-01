from django.urls import path

from . import views

app_name = 'appts'
urlpatterns = [
    path("", views.ApptsIndexView.as_view(), name="index"),
    ]
