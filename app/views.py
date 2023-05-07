from django.shortcuts import render
import random

def index(request):
    links = [
        { 'name': 'Home', 'url': 'home'},
        { 'name': 'About', 'url': 'about'},
        { 'name': 'Experience', 'url': 'experience'},
        { 'name': 'Project', 'url': 'project'},
        { 'name': 'Blog', 'url': 'blog'}
    ]
    project = ['1', '2', '3', '4', '5', '6']
    blog = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    blog = random.sample(blog, 6)
    context = { 'links': links, 'request': request, 'project': project, 'blog': blog }
    return render(request,'index.html', context)