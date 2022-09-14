from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='index'),
	path('home/', views.home, name='home'),
	path('projects/', views.projects, name='projects'),

]

