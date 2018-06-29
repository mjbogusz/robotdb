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
	path('applications/', views.ApplicationListView.as_view(), name = 'applicationList'),
	path('applications/add/', views.ApplicationCreateView.as_view(), name = 'applicationCreate'),
	path('applications/<int:applicationID>/', views.ApplicationDetailView.as_view(), name = 'applicationDetail'),
	path('applications/<int:applicationID>/edit/', views.ApplicationUpdateView.as_view(), name = 'applicationUpdate'),
	path('articles/', views.ArticleListView.as_view(), name = 'articleList'),
	path('articles/add/', views.ArticleCreateView.as_view(), name = 'articleCreate'),
	path('articles/<int:articleID>/', views.ArticleDetailView.as_view(), name = 'articleDetail'),
	path('articles/<int:articleID>/edit/', views.ArticleUpdateView.as_view(), name = 'articleUpdate'),
	path('features/', views.FeatureListView.as_view(), name = 'featureList'),
	path('features/add/', views.FeatureCreateView.as_view(), name = 'featureCreate'),
	path('features/<int:featureID>/', views.FeatureDetailView.as_view(), name = 'featureDetail'),
	path('features/<int:featureID>/edit/', views.FeatureUpdateView.as_view(), name = 'featureUpdate'),
	path('projects/', views.ProjectListView.as_view(), name = 'projectList'),
	path('projects/add/', views.ProjectCreateView.as_view(), name = 'projectCreate'),
	path('projects/<int:projectID>/', views.ProjectDetailView.as_view(), name = 'projectDetail'),
	path('projects/<int:projectID>/edit/', views.ProjectUpdateView.as_view(), name = 'projectUpdate'),
	path('robots/', views.RobotListView.as_view(), name = 'robotList'),
	path('robots/add/', views.RobotCreateView.as_view(), name = 'robotCreate'),
	path('robots/<int:robotID>/', views.RobotDetailView.as_view(), name = 'robotDetail'),
	path('robots/<int:robotID>/edit/', views.RobotUpdateView.as_view(), name = 'robotUpdate'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
