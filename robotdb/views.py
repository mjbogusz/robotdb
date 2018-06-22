from django.shortcuts import render
from django_tables2 import RequestConfig

from django.http import HttpResponse
from django.template import loader
from .models import Application, Article, Feature, Project, Robot
from .tables import ApplicationTable

def index(request):
	return render(request, 'index.html')

def applicationList(request):
	applicationTable = ApplicationTable(Application.objects.all())
	RequestConfig(request).configure(applicationTable)
	return render(request, 'applicationList.html', {'applicationTable': applicationTable})

def applicationDetail(request, applicationID):
	template = loader.get_template('applicationDetails.html')
	context = {
		'application': Application.objects.get(id = applicationID)
	}
	return HttpResponse(template.render(context, request))

def articleList(request):
	template = loader.get_template('articleList.html')
	context = {
		'articleList': Article.objects.all()
	}
	return HttpResponse(template.render(context, request))

def articleDetail(request, articleID):
	template = loader.get_template('articleDetails.html')
	context = {
		'article': Article.objects.get(id = articleID)
	}
	return HttpResponse(template.render(context, request))

def featureList(request):
	template = loader.get_template('featureList.html')
	context = {
		'featureList': Feature.objects.all()
	}
	return HttpResponse(template.render(context, request))

def featureDetail(request, featureID):
	template = loader.get_template('featureDetails.html')
	context = {
		'feature': Feature.objects.get(id = featureID)
	}
	return HttpResponse(template.render(context, request))

def projectList(request):
	template = loader.get_template('projectList.html')
	context = {
		'projectList': Project.objects.all()
	}
	return HttpResponse(template.render(context, request))

def projectDetail(request, projectID):
	template = loader.get_template('projectDetails.html')
	context = {
		'project': Project.objects.get(id = projectID)
	}
	return HttpResponse(template.render(context, request))

def robotList(request):
	template = loader.get_template('robotList.html')
	context = {
		'robotList': Robot.objects.all()
	}
	return HttpResponse(template.render(context, request))

def robotDetail(request, robotID):
	template = loader.get_template('robotDetails.html')
	context = {
		'robot': Robot.objects.get(id = robotID)
	}
	return HttpResponse(template.render(context, request))
