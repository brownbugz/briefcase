from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Photo


#classes
class ProjectCreate(CreateView):
    model = Project
    fields = ['user', 'profile_link', 'github_link', 'about_me']

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['github_link', 'about_me']

class ProjectDelete(DeleteView):
    model = Project
    sucess_url = '/projects/'

#functions
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')