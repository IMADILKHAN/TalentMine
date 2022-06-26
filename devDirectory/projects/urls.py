from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing,name="landing"),
    path('feed', views.feed,name="feed"),
    path('feed/upload', views.uploadPost,name="feed-upload"),
    path('project/', views.projects,name="projects"),
    path('project/<str:pk>/', views.project,name="project"),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:pk>/',views.updateProject,name="update-project"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project"),

]
