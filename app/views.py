from django.shortcuts import render

def index(request):
    links = [
        { 'name': 'Home', 'url': 'home'},
        { 'name': 'About', 'url': 'about'},
        { 'name': 'Blog', 'url': 'blog'}
    ]
    context = { 'links': links, 'request': request }
    return render(request,'home.html', context)