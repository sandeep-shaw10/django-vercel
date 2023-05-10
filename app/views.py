from django.shortcuts import render
from .models import PersonalData, Experience


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

    skills = [('Java', 70), ('Python', 82), ('C++', 170),('Bash', 80),('Photoshop', 80),('Figma', 80)]
    project = ['1', '2', '3', '4', '5', '6']
    context = { 'links': links, 'personal': personal, 'experiences': experiences, 'project': project, 'skills': skills }
    return render(request,'index.html', context)