import django_tables2 as tables
from django.utils.html import format_html
from ..models import Robot

class RobotImageColumn(tables.Column):
	def render(self, record, value):
		robotImages = value.all()
		html = ''
		if (len(robotImages)):
			html += '<ul class="robotImageList">\n'
			for robotImage in robotImages:
				html += format_html('<li><a href="{}"><img src="{}" /></a></li>\n', robotImage.image.url, robotImage.thumbnail.url)
			html += '</u>'
		return format_html(html)

class RobotTable(tables.Table):
	link = tables.Column(orderable = False)
	videoLink = tables.Column(orderable = False)
	notes = tables.Column(orderable = False)
	robotimage_set = RobotImageColumn(verbose_name = 'Images', orderable = False, attrs = {
		'th': {'class': 'tableImageList'},
		'td': {'class': 'tableImageList'}
	})

	def render_name(self, record, value):
		return format_html('<a href="/robots/{}/">{}</a>', record.id, value)

	def render_link(self, value):
		return format_html('<a href="{}">LINK</a>', value)

	def render_videoLink(self, value):
		return format_html('<a href="{}">VIDEO LINK</a>', value)

	class Meta:
		model = Robot
		attrs = {
			'class': 'robotTable pure-table'
		}
