from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django.urls import reverse

from django_tables2.views import SingleTableMixin
# from django_filters.views import FilterView

from robotdb.models import Equipment
from robotdb.tables import EquipmentTable

class EquipmentCreateView(LoginRequiredMixin, CreateView):
	model = Equipment
	template_name = 'views/equipment/create.html'
	fields = (
		'name',
		'parameters',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(EquipmentCreateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

class EquipmentDetailView(LoginRequiredMixin, DetailView):
	model = Equipment
	template_name = 'views/equipment/detail.html'
	context_object_name = 'equipment'
	pk_url_kwarg = 'equipmentID'

class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
	model = Equipment
	template_name = 'views/equipment/update.html'
	pk_url_kwarg = 'equipmentID'

	fields = (
		'name',
		'parameters',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(EquipmentUpdateView, self).get_form(**kwargs)
		form.fields['notes'].widget = widgets.Textarea()
		return form

# class EquipmentListView(LoginRequiredMixin, SingleTableMixin, FilterView):
class EquipmentListView(LoginRequiredMixin, SingleTableMixin, ListView):
	model = Equipment
	template_name = 'views/list.html'

	table_class = EquipmentTable
	paginate_by = False
	table_pagination = False
	# filterset_class = EquipmentFilter

	def get_context_data(self, **kwargs):
		context = super(EquipmentListView, self).get_context_data(**kwargs)

		context['title'] = 'Equipments'
		context['addButton'] = {
			'url': reverse('equipmentCreate'),
			'title': 'Add an equipment',
		}

		return context

	def get_table_pagination(self, table):
		return False
