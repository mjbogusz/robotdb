from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Article
from robotdb.tables import ArticleTable

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'articleCreate.html'
	fields = (
		'name',
		'link',
		'year',
		'bibtex',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(ArticleCreateView, self).get_form(**kwargs)
		form.fields['bibtex'].widget = widgets.Textarea()
		form.fields['notes'].widget = widgets.Textarea()
		return form

class ArticleDetailView(DetailView):
	model = Article
	template_name = 'articleDetail.html'
	context_object_name = 'article'
	pk_url_kwarg = 'articleID'

class ArticleUpdateView(UpdateView):
	model = Article
	template_name = 'articleUpdate.html'
	pk_url_kwarg = 'articleID'

	fields = (
		'name',
		'link',
		'year',
		'bibtex',
		'notes',
	)

	def get_form(self, **kwargs):
		form = super(ArticleUpdateView, self).get_form(**kwargs)
		form.fields['bibtex'].widget = widgets.Textarea()
		form.fields['notes'].widget = widgets.Textarea()
		return form

class ArticleListView(ListView):
	model = Article
	template_name = 'articleList.html'

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)
		articleQuerySet = Article.objects.all()
		articleTable = ArticleTable(articleQuerySet, exclude = ('bibtex',))
		RequestConfig(self.request).configure(articleTable)
		context['articleTable'] = articleTable
		context['articleCount'] = len(articleQuerySet)
		return context
