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

def tulane(request):
    return render(request, 'main/tulane.html')


def hobby(request):
    return render(request, 'main/hobby.html')


def professional(request):
    return render(request, 'main/professional.html')

def extracurricular(request):
    return render(request, 'main/extracurricular.html')