from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Project
from robotdb.tables import ProjectTable

class ProjectCreateView(CreateView):
	model = Project
	template_name = 'projectCreate.html'
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

class ProjectDetailView(DetailView):
	model = Project
	template_name = 'projectDetail.html'
	context_object_name = 'project'
	pk_url_kwarg = 'projectID'

class ProjectUpdateView(UpdateView):
	model = Project
	template_name = 'projectUpdate.html'
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

class ProjectListView(ListView):
	model = Project
	template_name = 'projectList.html'

	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)
		projectQuerySet = Project.objects.all()
		projectTable = ProjectTable(projectQuerySet)
		RequestConfig(self.request).configure(projectTable)
		context['projectTable'] = projectTable
		context['projectCount'] = len(projectQuerySet)
		return context