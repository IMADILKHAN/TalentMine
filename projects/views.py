from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Project,Tag,Jobs
from .forms import ProjectForm,ReviewForm
from .utils import searchProject,paginateProjects,getJobs,paginateJobs



def resume(request):
    return render(request,'projects/resume.html')


def landing(request):
    context = {}
    return render(request,'projects/landing.html',context)



def jobPostings(request):
    search_query,jobs = getJobs(request)
    custom_range,jobs = paginateJobs(request,jobs,6)
    context = {'jobs':jobs,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/jobs.html',context)

def jobPosting(request,pk):
    job = Jobs.objects.get(id=pk)
    return render(request,'projects/job.html',{'job':job})

def projects(request):
    search_query,projects = searchProject(request)

    custom_range,projects = paginateProjects(request,projects,6)

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




@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method =='POST':
        newtags = request.POST.get('newtags').replace(',',' ').split()
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')
    context = {'form':form}
    return render(request,"projects/project_form.html",context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method =='POST':
        newtags = request.POST.get('newtags').replace(',',' ').split()
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
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
