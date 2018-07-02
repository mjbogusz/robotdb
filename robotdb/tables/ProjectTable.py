from django.utils.html import format_html
from django.urls import reverse
import django_tables2 as tables

from robotdb.models import Project

class ProjectTable(tables.Table):
	link = tables.Column(orderable = False)
	notes = tables.Column(orderable = False)

	def render_id(self, record, value):
		href = reverse('projectDetail', kwargs = {'projectID': record.id})
		return format_html('<a href="{}">{}</a>', href, value)

	def render_name(self, record, value):
		return self.render_id(record, value)

	def render_link(self, value):
		return format_html('<a href="{}">LINK</a>', value)

	class Meta:
		model = Project
		attrs = {
			'class': 'projectTable entryTable pure-table'
		}
