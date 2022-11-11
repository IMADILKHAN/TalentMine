from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing,name="landing"),
    path('resume',views.resume,name="resume"),
    path('project/', views.projects,name="projects"),
    path('jobs/', views.jobPostings,name="jobPostings"),
    path('jobs/<str:pk>/', views.jobPosting,name="jobPosting"),
    path('project/<str:pk>/', views.project,name="project"),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:pk>/',views.updateProject,name="update-project"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project"),

]
