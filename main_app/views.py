from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Photo, Portfolio
from .models import Project, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'briefcase-group'


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


def add_photo(request, project_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, project_id=project_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', project_id=project_id)  

