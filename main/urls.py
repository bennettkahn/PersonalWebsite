from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='index'),
	path('home/', views.home, name='home'),
	path('tulane/', views.tulane, name='tulane'),
	path('hobby/', views.hobby, name='hobby'),
	path('professional/', views.professional, name='professional'),
	path('extracurricular/', views.extracurricular, name='extracurricular'),

]

