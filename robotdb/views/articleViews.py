from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.forms import widgets
from django.urls import reverse

from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

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

# class ArticleListView(LoginRequiredMixin, SingleTableMixin, FilterView):
class ArticleListView(LoginRequiredMixin, SingleTableMixin, ListView):
	model = Article
	template_name = 'views/list.html'

	table_class = ArticleTable
	paginate_by = False
	table_pagination = False
	# filterset_class = ArticleFilter

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)

		context['title'] = 'Articles'
		context['addButton'] = {
			'url': reverse('articleCreate'),
			'title': 'Add an article',
		}

		return context

	def get_table_pagination(self, table):
		return False
