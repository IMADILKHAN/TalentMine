from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serialized = ProjectSerializer(projects,many=True).data
    return Response(serialized)

@api_view(['GET'])
def getProject(request,pk):
    projects = Project.objects.get(id=pk)
    serialized = ProjectSerializer(projects).data
    return Response(serialized)
