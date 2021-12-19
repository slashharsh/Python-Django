from django.shortcuts import render
from django.http import HttpResponse            #All ABM

# Create your views here.

def projects(request):
    return render(request, 'projects/projects.html')
    # return HttpResponse("This is a list of all the projects")

def project(request,pk):
    return render(request, 'projects/single-project.html')
    # return HttpResponse("Single Project"+ " "+ pk)


