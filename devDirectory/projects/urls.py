from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects,name="all projects"),
    path('project/<str:pk>/', views.project,name="adils projects"),
]
