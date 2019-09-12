from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

#Portfolio Model
class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profile_link = models.CharField(max_length=100) #
    github_link = models.CharField(max_length=100)
    about_me = models.TextField(max_length=800)

    def __str__(self):
        return f'{self.id}: {self.user.username} portfolio'

#Project Model
class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=20)
    technologies = models.TextField(max_length=200)
    deployed_link = models.CharField(max_length=100)
    project_link = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return f'{self.portfolio.user.username} Project: {self.id} {self.project}'

#Photo Model
class Photo(models.Model):
    project = models.OneToOneField(Project, on_delete = models.CASCADE)
    portfolio = models.OneToOneField(Portfolio, on_delete = models.CASCADE)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f'Project: {self.project_id} @{self.url}\n portfolio: {self.portfolio_id} @{self.url}'