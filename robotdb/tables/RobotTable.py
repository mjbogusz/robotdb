from django.utils.html import format_html
from django.urls import reverse
import django_tables2 as tables

from robotdb.models import Robot

class RobotTable(tables.Table):
	link = tables.Column(orderable = False)
	videoLink = tables.Column(orderable = False)
	notes = tables.Column(orderable = False)
	equipment = tables.Column(orderable = False, attrs = {
		'th': {'class': 'equipmentList'},
		'td': {'class': 'equipmentList'}
	})
	skills = tables.Column(orderable = False)
	articles = tables.Column(orderable = False)
	projects = tables.Column(orderable = False)
	robotimage_set = tables.Column(verbose_name = 'Pictures', orderable = False, attrs = {
		'th': {'class': 'tableImageList'},
		'td': {'class': 'tableImageList'}
	})

	def render_id(self, record, value):
		href = reverse('robotDetail', kwargs = {'robotID': record.id})
		return format_html('<a href="{}">{}</a>', href, value)

	def render_name(self, record, value):
		return self.render_id(record, value)

	def render_link(self, value):
		return format_html('<a href="{}">LINK</a>', value)

	def render_videoLink(self, value):
		links = value.split('\n')
		if len(links) > 1:
			html = '<ul>'
			for i in links:
				html += format_html('<li><a href="{}">VIDEO</a></li>', i)
			html += '</ul>'
		else:
			html = format_html('<a href="{}">VIDEO</a>', value)
		return format_html(html)

	def render_skills(self, value):
		skills = value.all()
		html = '<ul class="skillList">'
		for i in skills:
			href = reverse('skillDetail', kwargs = {'skillID': i.id})
			html += format_html('<li><a href="{}">{}</a></li>', href, i)
		html += '</ul>'
		return format_html(html)

	def render_articles(self, value):
		articles = value.all()
		html = '<ul class="articleList">'
		for i in articles:
			href = reverse('articleDetail', kwargs = {'articleID': i.id})
			html += format_html('<li><a href="{}">{}</a></li>', href, i)
		html += '</ul>'
		return format_html(html)

	def render_equipment(self, record, value):
		robotEquipments = record.robotequipment_set.filter(available = True).order_by('equipment')
		html = '<ul class="equipmentList">'
		for i in robotEquipments:
			href = reverse('equipmentDetail', kwargs = {'equipmentID': i.id})
			html += format_html('<li><a href="{}">{}</a></li>', href, i.equipment)
		html += '</ul>'
		return format_html(html)

	def render_projects(self, value):
		projects = value.all()
		html = '<ul class="projectList">'
		for i in projects:
			href = reverse('projectDetail', kwargs = {'projectID': i.id})
			html += format_html('<li><a href="{}">{}</a></li>', href, i)
		html += '</ul>'
		return format_html(html)

	def render_robotimage_set(self, value):
		robotImages = value.all()
		html = ''
		if (len(robotImages)):
			html += '<ul class="robotImageList">\n'
			for robotImage in robotImages:
				html += format_html('<li><a href="{}"><img src="{}" /></a></li>\n', robotImage.image.url, robotImage.thumbnail.url)
			html += '</u>'
		return format_html(html)

	class Meta:
		model = Robot
		attrs = {
			'class': 'entryTable pure-table'
		}
		empty_text = 'No robots in database.'
