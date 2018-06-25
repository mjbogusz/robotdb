from django.shortcuts import render, get_object_or_404
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
	application = get_object_or_404(Application, pk = applicationID)
	return render(request, 'applicationDetails.html', {
		'application': application
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
	article = get_object_or_404(Article, pk = articleID)
	return render(request, 'articleDetails.html', {
		'article': article
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
	feature = get_object_or_404(Feature, pk = featureID)
	return render(request, 'featureDetails.html', {
		'feature': feature
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
	project = get_object_or_404(Project, pk = projectID)
	return render(request, 'projectDetails.html', {
		'project': project
	})

def robotList(request):
	robots = Robot.objects.all()
	robotTable = RobotTable(robots)
	RequestConfig(request).configure(robotTable)
	return render(request, 'robotList.html', {
		'count': len(robots),
		'robotTable': robotTable,
	})

def robotEdit(request, robotID):
	if robotID:
		robot = get_object_or_404(Robot, pk = robotID)
	else:
		robot = None

	applications = Application.objects.all()
	articles = Article.objects.all()
	features = Feature.objects.all()
	projects = Project.objects.all()

	if request.method == 'GET':
		return render(request, 'robotEdit.html', {
			'robot': robot,
			'applications': applications,
			'articles': articles,
			'features': features,
			'projects': projects,
		})

def robotView(request, robotID):
	robot = Robot.objects.get(id = robotID)
	knownFeatureIDs = robot.robotfeature_set.all().values_list('feature_id', flat = True)
	unknownFeatures = Feature.objects.exclude(id__in = knownFeatureIDs)
	return render(request, 'robotView.html', {
		'robot': Robot.objects.get(id = robotID),
		'unknownFeatures': unknownFeatures
	})
