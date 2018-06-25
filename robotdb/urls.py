"""robotdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# Application, Article, Feature, Project, Robot

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.index, name = 'index'),
	path('applications', views.applicationList, name = 'applicationList'),
	path('applications/<int:applicationID>/', views.applicationDetail, name = 'applicationDetail'),
	path('articles', views.articleList, name = 'articleList'),
	path('articles/<int:articleID>/', views.articleDetail, name = 'articleDetail'),
	path('features', views.featureList, name = 'featureList'),
	path('features/<int:featureID>/', views.featureDetail, name = 'featureDetail'),
	path('projects', views.projectList, name = 'projectList'),
	path('projects/<int:projectID>/', views.projectDetail, name = 'projectDetail'),
	path('robots', views.robotList, name = 'robotList'),
	path('robots/add/', views.robotEdit, name = 'robotAdd'),
	path('robots/<int:robotID>/', views.robotView, name = 'robotView'),
	path('robots/<int:robotID>/edit', views.robotEdit, name = 'robotEdit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
