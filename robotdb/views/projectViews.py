from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django.urls import reverse

from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from robotdb.models import Project
from robotdb.tables import ProjectTable

class ProjectCreateView(LoginRequiredMixin, CreateView):
	model = Project
	template_name = 'views/project/create.html'
	fields = (
		'name',
		'link',
		'year',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(ProjectCreateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class ProjectDetailView(LoginRequiredMixin, DetailView):
	model = Project
	template_name = 'views/project/detail.html'
	context_object_name = 'project'
	pk_url_kwarg = 'projectID'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
	model = Project
	template_name = 'views/project/update.html'
	pk_url_kwarg = 'projectID'

	fields = (
		'name',
		'link',
		'year',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(ProjectUpdateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

# class ProjectListView(LoginRequiredMixin, SingleTableMixin, FilterView):
class ProjectListView(LoginRequiredMixin, SingleTableMixin, ListView):
	model = Project
	template_name = 'views/list.html'

	table_class = ProjectTable
	paginate_by = False
	table_pagination = False
	# filterset_class = ProjectFilter

	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)

		context['title'] = 'Projects'
		context['addButton'] = {
			'url': reverse('projectCreate'),
			'title': 'Add a project',
		}

		return context

	def get_table_pagination(self, table):
		return False
