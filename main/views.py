from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


'''
class HomeView(TemplateView):
	template_name = "main/home.html"


class ProjectsView(TemplateView):
	template_name = "main/projects.html"
'''

def home(request):
    return render(request, 'main/home.html')

def projects(request):
    return render(request, 'main/projects.html')