from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Project

class ProjectCreate(CreateView):
    model = Project
    fields = ['user', 'profile_link', 'github_link', 'about_me']


def home(request):
    return render(request, 'home.html')