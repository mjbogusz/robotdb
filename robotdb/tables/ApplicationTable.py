import django_tables2 as tables
from ..models import Application

class ApplicationTable(tables.Table):
	class Meta:
		model = Application
		attrs = {
			'class': 'applicationTable pure-table'
		}
