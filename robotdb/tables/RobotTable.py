import django_tables2 as tables
from django.utils.html import format_html
from robotdb.models import Feature, Robot

class RobotTable(tables.Table):
	link = tables.Column(orderable = False)
	videoLink = tables.Column(orderable = False)
	notes = tables.Column(orderable = False)
	features = tables.Column(orderable = False, attrs = {
		'th': {'class': 'featureList'},
		'td': {'class': 'featureList'}
	})
	applications = tables.Column(orderable = False)
	articles = tables.Column(orderable = False)
	projects = tables.Column(orderable = False)
	robotimage_set = tables.Column(verbose_name = 'Pictures', orderable = False, attrs = {
		'th': {'class': 'tableImageList'},
		'td': {'class': 'tableImageList'}
	})

	def render_id(self, record, value):
		return format_html('<a href="/robots/{}/">{}</a>', record.id, value)

	def render_name(self, record, value):
		return format_html('<a href="/robots/{}/">{}</a>', record.id, value)

	def render_link(self, value):
		return format_html('<a href="{}">LINK</a>', value)

	def render_videoLink(self, value):
		return format_html('<a href="{}">VIDEO LINK</a>', value)

	def render_applications(self, value):
		applications = value.all()
		html = '<ul class="applicationList">'
		for i in applications:
			html += format_html('<li><a href="applications/{}/">{}</a></li>', i.id, i)
		html += '</ul>'
		return format_html(html)

	def render_articles(self, value):
		articles = value.all()
		html = '<ul class="articleList">'
		for i in articles:
			html += format_html('<li><a href="articles/{}/">{}</a></li>', i.id, i)
		html += '</ul>'
		return format_html(html)

	def render_features(self, record, value):
		html = ''
		robotFeatures = record.robotfeature_set.all().order_by('-available', 'feature')
		for rf in robotFeatures:
			if rf.available:
				html += '<p><span class="feature_true">✔</span> '
			else:
				html += '<p><span class="feature_false">✘</span> '
			html += format_html('<a href="features/{}/">{}</a>', rf.feature_id, rf.feature)
			html += '</p>'

		knownFeatureIDs = robotFeatures.values_list('feature_id', flat = True)
		unknownFeatures = Feature.objects.exclude(id__in = knownFeatureIDs)
		for f in unknownFeatures:
			html += '<p><span class="feature_unknown">?</span> '
			html += format_html('<a href="features/{}/">{}</a>', f.id, f)
			html += '</p>'

		return format_html(html)

	def render_projects(self, value):
		projects = value.all()
		html = '<ul class="projectList">'
		for i in projects:
			html += format_html('<li><a href="projects/{}/">{}</a></li>', i.id, i)
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
			'class': 'robotTable pure-table'
		}
