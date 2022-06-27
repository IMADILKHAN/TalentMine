from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm,PostForm
from .utils import searchProject,paginateProjects,getPosts


def landing(request):
    context = {}
    return render(request,'projects/landing.html',context)

def feed(request):
    posts = getPosts(request)
    if request.user.is_authenticated:
        user = request.user.profile
    else:
        user = None
    context = {'posts':posts,'user':user}

    return render(request,'projects/feed.html',context)

def projects(request):
    search_query,projects = searchProject(request)

    custom_range,projects = paginateProjects(request,projects,3)

    context = {'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        projectObj.getVoteCount
        return redirect('project',pk=projectObj.id)

    context = {
        'project':projectObj,
        'form':form,

    }
    return render(request,'projects/single-project.html',context)

@login_required(login_url = 'login')
def uploadPost(request):
    profile = request.user.profile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = profile
            post.save()
            return redirect('feed')
    context = {'form':form}
    return render(request,"projects/post_form.html",context)

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,"projects/project_form.html",context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,"projects/project_form.html",context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'delete_template.html',context)
