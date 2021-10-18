from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
        {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website'},
        {
        'id':'2',
        'title':'Fayur',
        'description':"Website To make artist and venur's meet"},
        {
        'id':'3',
        'title':'Craigs List',
        'description':"Craigs List Clone"},]





def projects(request):
    page = 'projects'
    number = 11
    context = {'msg':page,'num':number,'projects':projectsList}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = None
    for i in projectsList:
        if i['id']==pk:
            projectObj = i
            break
    # print(projectObj)
    return render(request,'projects/single-project.html',{'project':projectObj})
