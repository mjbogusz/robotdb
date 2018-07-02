from django import forms
from django.contrib import admin

from robotdb.models import Article

class ArticleAdminForm(forms.ModelForm):
	bibtex = forms.CharField(widget = forms.Textarea, required = False)
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Article
		exclude = ()

class ArticleAdmin(admin.ModelAdmin):
	form = ArticleAdminForm
	fieldsets = [
		(None, {'fields': [
			'name',
			'year',
			'link',
		]}),
		('BibTeX', {'fields': [
			'bibtex',
		]}),
		('Notes', {'fields': [
			'notes',
		]}),
	]

	list_display = [
		'name',
		'year',
		'link',
	]
	list_filter = [
		'year',
	]
	search_fields = [
		'name',
		'bibtex',
		'notes',
	]
