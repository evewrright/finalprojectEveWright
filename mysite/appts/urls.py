from django.urls import path

from . import views

app_name = 'appts'
urlpatterns = [
    path("", views.ApptsIndexView.as_view(), name="index"),
    path('detail/<int:pk>/', views.ApptsDetailView.as_view(), name='detail'),
    path("create", views.ApptsCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.ApptsUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ApptsDeleteView.as_view(), name="delete"),
    path('generate-paragraph/', views.generate_paragraph, name='generate-paragraph'),
    path('paragraph/', views.ParagraphView.as_view(), name="paragraph"),
    path('history/', views.historyview, name="history")
    ]
