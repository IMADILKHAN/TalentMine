from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are the projects')

def project(request):
    return HttpResponse('Particular projects')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects,name="all projects"),
    path('project/', project,name="adils projects"),
]
