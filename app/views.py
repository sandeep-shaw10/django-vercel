from django.shortcuts import render
from .models import PersonalData, Experience, Skill, Project


def index(request):
    links = [
        { 'name': 'Home', 'url': 'home'},
        { 'name': 'About', 'url': 'about'},
        { 'name': 'Experience', 'url': 'experience'},
        { 'name': 'Project', 'url': 'project'},
        { 'name': 'Skills', 'url': 'skills'},
    ]

    personal = experiences = skills = projects = error = None
    try:
        personal = PersonalData.objects.latest('id')
        experiences = Experience.objects.all().order_by('-start_date')
        skills = Skill.objects.all().order_by('-percentage')
        projects = Project.objects.filter(is_archived=False).order_by('-date')
    except Exception as e:
        error = e

    context = { 
        'links': links, 
        'personal': personal, 
        'experiences': experiences, 
        'projects': projects, 
        'skills': skills,
        'error': error 
    }
    
    return render(request,'index.html', context)