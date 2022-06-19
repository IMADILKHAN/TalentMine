from .models import Project,Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def searchProject(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tag = Tag.objects.filter(name__icontains=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query)|
        Q(description__icontains=search_query)|
        Q(owner__name__icontains=search_query)|
        Q(tags__in=tag)
    )
    return search_query,projects

def paginateProjects(request,projects,results):
    page = request.GET.get('page')
    paginator = Paginator(projects,results)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = max(int(page)-1,1)
    rightIndex = min(int(page)+2,paginator.num_pages+1)
    custom_range = range(leftIndex,rightIndex)

    return custom_range,projects
