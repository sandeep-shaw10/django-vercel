from django.http import HttpResponse
from core.utils.user import allUsers


def index(request):
    data = allUsers()
    if(data['error']):
        return HttpResponse(f"Error fetching user: {data['error']}")
    else:
        names = ''
        for i in data['users']:
            names += f"{i} "
        return HttpResponse(f"User: {names}")