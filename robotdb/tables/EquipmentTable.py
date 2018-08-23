from django.utils.html import format_html
from django.urls import reverse
import django_tables2 as tables

from robotdb.models import Equipment

class EquipmentTable(tables.Table):
	notes = tables.Column(orderable = False)

	def render_id(self, record, value):
		href = reverse('equipmentDetail', kwargs = {'equipmentID': record.id})
		return format_html('<a href="{}">{}</a>', href, value)

	def render_name(self, record, value):
		return self.render_id(record, value)

	class Meta:
		model = Equipment
		attrs = {
			'class': 'entryTable pure-table'
		}
		empty_text = 'No equipment in database.'
