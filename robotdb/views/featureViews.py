from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Feature
from robotdb.tables import FeatureTable

class FeatureCreateView(LoginRequiredMixin, CreateView):
	model = Feature
	template_name = 'views/feature/create.html'
	fields = (
		'name',
		'parameters',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(FeatureCreateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class FeatureDetailView(LoginRequiredMixin, DetailView):
	model = Feature
	template_name = 'views/feature/detail.html'
	context_object_name = 'feature'
	pk_url_kwarg = 'featureID'

class FeatureUpdateView(LoginRequiredMixin, UpdateView):
	model = Feature
	template_name = 'views/feature/update.html'
	pk_url_kwarg = 'featureID'

	fields = (
		'name',
		'parameters',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(FeatureUpdateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class FeatureListView(LoginRequiredMixin, ListView):
	model = Feature
	template_name = 'views/feature/list.html'

	def get_context_data(self, **kwargs):
		context = super(FeatureListView, self).get_context_data(**kwargs)
		featureQuerySet = Feature.objects.all()
		featureTable = FeatureTable(featureQuerySet)
		RequestConfig(self.request).configure(featureTable)
		context['featureTable'] = featureTable
		context['featureCount'] = len(featureQuerySet)
		return context
