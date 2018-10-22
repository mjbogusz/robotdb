from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django.urls import reverse

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from robotdb.models import Robot
from robotdb.tables import RobotTable
from robotdb.filters import RobotFilter

class RobotCreateView(LoginRequiredMixin, CreateView):
	model = Robot
	template_name = 'views/robot/create.html'
	fields = (
		'name',
		'producer',
		'country',
		'year',
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
		'year',
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

class RobotListView(LoginRequiredMixin, SingleTableMixin, FilterView):
	model = Robot
	template_name = 'views/list.html'

	table_class = RobotTable
	paginate_by = False
	table_pagination = False
	filterset_class = RobotFilter

	def get_filterset_kwargs(self, filterset_class):
		kwargs = super(RobotListView, self).get_filterset_kwargs(filterset_class)
		if kwargs['data'] is None:
			kwargs['data'] = {}
		return kwargs

	def get_context_data(self, **kwargs):
		context = super(RobotListView, self).get_context_data(**kwargs)
		context['title'] = 'Robots'
		context['addButton'] = {
			'url': reverse('robotCreate'),
			'title': 'Add a robot',
		}
		return context

	def get_table_pagination(self, table):
		return False
