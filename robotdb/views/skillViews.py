from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django.urls import reverse

from django_tables2.views import SingleTableMixin
# from django_filters.views import FilterView

from robotdb.models import Skill
from robotdb.tables import SkillTable

class SkillCreateView(LoginRequiredMixin, CreateView):
	model = Skill
	template_name = 'views/skill/create.html'
	fields = (
		'name',
		'mobility',
		'selfreliantCare',
		'interpersonalInteraction',
		'other',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(SkillCreateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class SkillDetailView(LoginRequiredMixin, DetailView):
	model = Skill
	template_name = 'views/skill/detail.html'
	context_object_name = 'skill'
	pk_url_kwarg = 'skillID'

class SkillUpdateView(LoginRequiredMixin, UpdateView):
	model = Skill
	template_name = 'views/skill/update.html'
	pk_url_kwarg = 'skillID'

	fields = (
		'name',
		'mobility',
		'selfreliantCare',
		'interpersonalInteraction',
		'other',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(SkillUpdateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

# class SkillListView(LoginRequiredMixin, SingleTableMixin, FilterView):
class SkillListView(LoginRequiredMixin, SingleTableMixin, ListView):
	model = Skill
	template_name = 'views/list.html'

	table_class = SkillTable
	paginate_by = False
	table_pagination = False
	# filterset_class = SkillFilter

	def get_context_data(self, **kwargs):
		context = super(SkillListView, self).get_context_data(**kwargs)

		context['title'] = 'Skills'
		context['addButton'] = {
			'url': reverse('skillCreate'),
			'title': 'Add an skill',
		}

		return context

	def get_table_pagination(self, table):
		return False
