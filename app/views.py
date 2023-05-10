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

    personal = PersonalData.objects.latest('id')
    experiences = Experience.objects.all().order_by('-start_date')
    skills = Skill.objects.all().order_by('-percentage')
    projects = Project.objects.filter(is_archived=False).order_by('-date')

    project = ['1', '2', '3', '4', '5', '6']
    context = { 'links': links, 'personal': personal, 'experiences': experiences, 'projects': projects, 'skills': skills }
    return render(request,'index.html', context)