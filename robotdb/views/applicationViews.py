from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Application
from robotdb.tables import ApplicationTable

class ApplicationCreateView(CreateView):
	model = Application
	template_name = 'applicationCreate.html'
	fields = (
		'name',
		'mobility',
		'selfreliantCare',
		'interpersonalInteraction',
		'other',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(ApplicationCreateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class ApplicationDetailView(DetailView):
	model = Application
	template_name = 'applicationDetail.html'
	context_object_name = 'application'
	pk_url_kwarg = 'applicationID'

class ApplicationUpdateView(UpdateView):
	model = Application
	template_name = 'applicationUpdate.html'
	pk_url_kwarg = 'applicationID'

	fields = (
		'name',
		'mobility',
		'selfreliantCare',
		'interpersonalInteraction',
		'other',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(ApplicationUpdateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class ApplicationListView(ListView):
	model = Application
	template_name = 'applicationList.html'

	def get_context_data(self, **kwargs):
		context = super(ApplicationListView, self).get_context_data(**kwargs)
		applicationQuerySet = Application.objects.all()
		applicationTable = ApplicationTable(applicationQuerySet)
		RequestConfig(self.request).configure(applicationTable)
		context['applicationTable'] = applicationTable
		context['applicationCount'] = len(applicationQuerySet)
		return context
