from django.urls import path

from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'
urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('login/', views.MyLoginView.as_view(), name='my-login'),
    path('logout/', LogoutView.as_view(next_page='main:my-login'), name='logout')
]
