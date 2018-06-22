from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Application, Article, Feature, Project, Robot
from .tables import ApplicationTable, ArticleTable, FeatureTable, ProjectTable, RobotTable

def index(request):
	return render(request, 'index.html')

def applicationList(request):
	applications = Application.objects.all()
	applicationTable = ApplicationTable(applications)
	RequestConfig(request).configure(applicationTable)
	return render(request, 'applicationList.html', {
		'count': len(applications),
		'applicationTable': applicationTable,
	})

def applicationDetail(request, applicationID):
	return render(request, 'applicationDetails.html', {
		'application': Application.objects.get(id = applicationID)
	})

def articleList(request):
	articles = Article.objects.all()
	articleTable = ArticleTable(articles)
	RequestConfig(request).configure(articleTable)
	return render(request, 'articleList.html', {
		'count': len(articles),
		'articleTable': articleTable,
	})

def articleDetail(request, articleID):
	return render(request, 'articleDetails.html', {
		'article': Article.objects.get(id = articleID)
	})

def featureList(request):
	features = Feature.objects.all()
	featureTable = FeatureTable(features)
	RequestConfig(request).configure(featureTable)
	return render(request, 'featureList.html', {
		'count': len(features),
		'featureTable': featureTable,
	})

def featureDetail(request, featureID):
	return render(request, 'featureDetails.html', {
		'feature': Feature.objects.get(id = featureID)
	})

def projectList(request):
	projects = Project.objects.all()
	projectTable = ProjectTable(projects)
	RequestConfig(request).configure(projectTable)
	return render(request, 'projectList.html', {
		'count': len(projects),
		'projectTable': projectTable,
	})

def projectDetail(request, projectID):
	return render(request, 'projectDetails.html', {
		'project': Project.objects.get(id = projectID)
	})

def robotList(request):
	robots = Robot.objects.all()
	robotTable = RobotTable(robots)
	RequestConfig(request).configure(robotTable)
	return render(request, 'robotList.html', {
		'count': len(robots),
		'robotTable': robotTable,
	})

def robotDetail(request, robotID):
	return render(request, 'robotDetails.html', {
		'robot': Robot.objects.get(id = robotID)
	})
