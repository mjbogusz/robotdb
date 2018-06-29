from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Robot, Feature
from robotdb.tables import RobotTable

class RobotCreateView(CreateView):
	model = Robot
	template_name = 'robotCreate.html'
	fields = (
		'name',
		'producer',
		'country',
		'link',
		'videoLink',
		'price',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(RobotCreateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class RobotDetailView(DetailView):
	model = Robot
	template_name = 'robotDetail.html'
	context_object_name = 'robot'
	pk_url_kwarg = 'robotID'

	def get_context_data(self, **kwargs):
		context = super(RobotDetailView, self).get_context_data(**kwargs)
		knownFeatureIDs = self.object.robotfeature_set.all().values_list('feature_id', flat = True)
		context['unknownFeatures'] = Feature.objects.exclude(id__in = knownFeatureIDs)
		return context

class RobotUpdateView(UpdateView):
	model = Robot
	template_name = 'robotUpdate.html'
	pk_url_kwarg = 'robotID'

	fields = (
		'name',
		'producer',
		'country',
		'link',
		'videoLink',
		'price',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(RobotUpdateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class RobotListView(ListView):
	model = Robot
	template_name = 'robotList.html'

	def get_context_data(self, **kwargs):
		context = super(RobotListView, self).get_context_data(**kwargs)
		robotQuerySet = Robot.objects.all()
		robotTable = RobotTable(robotQuerySet)
		RequestConfig(self.request).configure(robotTable)
		context['robotTable'] = robotTable
		context['robotCount'] = len(robotQuerySet)
		return context
