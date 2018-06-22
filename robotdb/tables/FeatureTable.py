import django_tables2 as tables
from django.utils.html import format_html
from ..models import Feature

class FeatureTable(tables.Table):
	notes = tables.Column(orderable = False)

	def render_name(self, record, value):
		return format_html('<a href="/features/{}/">{}</a>', record.id, value)

	class Meta:
		model = Feature
		attrs = {
			'class': 'featureTable pure-table'
		}
