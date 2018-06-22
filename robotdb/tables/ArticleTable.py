import django_tables2 as tables
from django.utils.html import format_html
from ..models import Article

class ArticleTable(tables.Table):
	link = tables.Column(orderable = False)
	bibtex = tables.Column(orderable = False)
	notes = tables.Column(orderable = False)

	def render_name(self, record, value):
		return format_html('<a href="/articles/{}/">{}</a>', record.id, value)

	def render_link(self, value):
		return format_html('<a href="{}">LINK</a>', value)

	class Meta:
		model = Article
		attrs = {
			'class': 'articleTable pure-table'
		}
