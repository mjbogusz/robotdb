from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Robot, Feature
from robotdb.tables import RobotTable

class RobotCreateView(LoginRequiredMixin, CreateView):
	model = Robot
	template_name = 'views/robot/create.html'
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
		form.fields['videoLink'].widget = widgets.Textarea()
		form.fields['notes'].widget = widgets.Textarea()
		return form

class RobotDetailView(LoginRequiredMixin, DetailView):
	model = Robot
	template_name = 'views/robot/detail.html'
	context_object_name = 'robot'
	pk_url_kwarg = 'robotID'

	def get_context_data(self, **kwargs):
		context = super(RobotDetailView, self).get_context_data(**kwargs)
		knownFeatureIDs = self.object.robotfeature_set.all().values_list('feature_id', flat = True)
		context['unknownFeatures'] = Feature.objects.exclude(id__in = knownFeatureIDs)
		links = context['robot'].videoLink.split('\n')
		if len(links) > 1:
			context['robot'].videoLinks = context['robot'].videoLink.split('\n')
		return context

class RobotUpdateView(LoginRequiredMixin, UpdateView):
	model = Robot
	template_name = 'views/robot/update.html'
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
		form.fields['videoLink'].widget = widgets.Textarea()
		form.fields['notes'].widget = widgets.Textarea()
		return form

class RobotListView(LoginRequiredMixin, ListView):
	model = Robot
	template_name = 'views/robot/list.html'

	def get_context_data(self, **kwargs):
		context = super(RobotListView, self).get_context_data(**kwargs)
		robotQuerySet = Robot.objects.all()
		robotTable = RobotTable(robotQuerySet)
		RequestConfig(self.request).configure(robotTable)
		context['robotTable'] = robotTable
		context['robotCount'] = len(robotQuerySet)
		return context
