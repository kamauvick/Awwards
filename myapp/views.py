from django.shortcuts import render

from .models import *


def home(request):
    current_user = request.user
    project_images = Project.fetch_all_images()
    params = {
        'all_images': project_images,
        'current_user': current_user,
    }
    return render(request, "main/home.html", params)
