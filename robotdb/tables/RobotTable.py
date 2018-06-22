import django_tables2 as tables
from django.utils.html import format_html
from ..models import Robot

class RobotImageColumn(tables.Column):
	def render(self, value):
		html = ''
		if (len(value)):
			html += '<ul class="robotImageList">\n'
			for robotImage in value:
				html += format_html('<li><a href="{}"><img src="{}" /></a></li>\n', robotImage.image.url, robotImage.image.url)
			html += '</u>'
		return html

class RobotTable(tables.Table):
	class Meta:
		model = Robot
		attrs = {
			'class': 'robotTable pure-table'
		}
