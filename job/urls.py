from .import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<str:nam>', views.all_job),
    path('<str:name>/<str:nam>/', views.single_post)
]