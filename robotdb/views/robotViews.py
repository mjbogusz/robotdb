from django.shortcuts import render, get_object_or_404, reverse
from django import forms
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect

from robotdb.models import Feature, Robot
from robotdb.tables import RobotTable

class RobotForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea)

	class Meta:
		model = Robot
		exclude = ()

def robotList(request):
	robots = Robot.objects.all()
	robotTable = RobotTable(robots)
	RequestConfig(request).configure(robotTable)
	return render(request, 'robotList.html', {
		'count': len(robots),
		'robotTable': robotTable,
	})

def robotEdit(request, robotID):
	# First, check if robot exists
	if robotID:
		robot = get_object_or_404(Robot, pk = robotID)
	else:
		robot = None

	# Then check if we're opening new add/edit view or handling sent data
	if request.method == 'GET':
		robotForm = RobotForm(instance = robot)
	else:
		robotForm = RobotForm(request.POST)

	# Display form with data
	if request.method == 'GET' or not robotForm.is_valid():
		return render(request, 'robotEdit.html', {
			'robotForm': robotForm.as_table(),
			'robot': robot,
		})

	# Handle valid sent data
	### TODO
	return HttpResponseRedirect(reverse('robotList'))

def robotView(request, robotID):
	robot = Robot.objects.get(id = robotID)
	knownFeatureIDs = robot.robotfeature_set.all().values_list('feature_id', flat = True)
	unknownFeatures = Feature.objects.exclude(id__in = knownFeatureIDs)
	return render(request, 'robotView.html', {
		'robot': Robot.objects.get(id = robotID),
		'unknownFeatures': unknownFeatures
	})
