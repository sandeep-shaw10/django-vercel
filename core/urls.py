"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from dotenv import load_dotenv
from django.contrib import admin
from django.urls import include, path

load_dotenv()

adminPath = os.getenv('ADMIN_PATH')
if(adminPath == None):
    adminPath = 'admin'

# Admin Display
admin.site.site_header = 'My Name'         
admin.site.index_title = 'Portfolio'
admin.site.site_title = 'Sandeep Shaw' 

urlpatterns = [
    path('', include("app.urls")),
    path(f'{adminPath}/', admin.site.urls),
]
