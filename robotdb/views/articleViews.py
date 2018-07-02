from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django_tables2 import RequestConfig

from robotdb.models import Article
from robotdb.tables import ArticleTable

class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = Article
	template_name = 'views/article/create.html'
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

class ArticleDetailView(LoginRequiredMixin, DetailView):
	model = Article
	template_name = 'views/article/detail.html'
	context_object_name = 'article'
	pk_url_kwarg = 'articleID'

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
	model = Article
	template_name = 'views/article/update.html'
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

class ArticleListView(LoginRequiredMixin, ListView):
	model = Article
	template_name = 'views/article/list.html'

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)
		articleQuerySet = Article.objects.all()
		articleTable = ArticleTable(articleQuerySet, exclude = ('bibtex',))
		RequestConfig(self.request).configure(articleTable)
		context['articleTable'] = articleTable
		context['articleCount'] = len(articleQuerySet)
		return context
