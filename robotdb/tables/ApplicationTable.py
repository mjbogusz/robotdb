import django_tables2 as tables
from django.utils.html import format_html
from ..models import Application

class ApplicationTable(tables.Table):
	notes = tables.Column(orderable = False)

	def render_name(self, record, value):
		return format_html('<a href="/applications/{}/">{}</a>', record.id, value)

	class Meta:
		model = Application
		attrs = {
			'class': 'applicationTable pure-table'
		}
