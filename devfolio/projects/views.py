from django.shortcuts import render
from django.http import HttpResponse            #All ABM
import datetime
# Create your views here.

projectslist = [
    {'id':'1','title':'E-Commerce','description':'Full E-Com project'},
    {'id':'2','title':'E-Commerce-2','description':'Full E-Com project-2'},
    {'id':'3','title':'E-Commerce-3','description':'Full E-Com project-3'},
    
]

def projects(request):
    age = 13
    msg = "You are on Project's page..!!"
    context = {'message':msg, 'date':datetime.date.today(),'projects':projectslist}
    return render(request, 'projects/projects.html',context)
    # return HttpResponse("This is a list of all the projects")

def project(request,pk):
    # age = 12
    msg = "This is "+""+pk+" project page!"
    projectObj = None
    for i in projectslist:
        if i['id'] == pk:
            projectObj = i
    context = {'message':msg, 'date':datetime.date.today(),'projects':projectObj}
    return render(request, 'projects/single-project.html',context)
    # return HttpResponse("Single Project"+ " "+ pk)


