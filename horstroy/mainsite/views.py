from django.views.generic.base import TemplateView
from django.shortcuts import render

from .models import Service, Project, DesignProject

def index(request):
    services = Service.objects.all()[:5]

    return render(
        request,
        'index.html',
        {
            'services': services,
        }
    )

def services(request):
    services = Service.objects.all()

    return render(
        request,
        'services.html',
        {
            'services': services,
            'page': 'services'
        }
    )

def technologies(request):
    return render(
        request,
        'technologies.html',
        {
            'page': 'technologies'
        }
    )

def materials(request):
    return render(
        request,
        'materials.html',
        {
            'page': 'materials'
        }
    )

def portfolio(request):
    projects = Project.objects.all()

    return render(
        request,
        'portfolio.html',
        {
            'projects': projects,
            'page': 'portfolio'
        }
    )

def designs(request):
    projects = DesignProject.objects.all()

    return render(
        request,
        'portfolio.html',
        {
            'projects': projects,
            'page': 'designs'
        }
    )

def error_404(request, exception):
   context = {}
   
   return render(request,'404.html', context)
