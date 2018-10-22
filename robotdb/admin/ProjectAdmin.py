from django import forms
from django.contrib import admin

from robotdb.models import Project

class ProjectAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Project
		exclude = ()

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminForm
	fieldsets = [
		(None, {'fields': [
			'name',
			'yearStart',
			'yearEnd',
			'link',
		]}),
		('Notes', {'fields': [
			'notes',
		]}),
	]

	list_display = [
		'name',
		'yearStart',
		'yearEnd',
		'link',
	]
	list_filter = [
		'yearStart',
		'yearEnd',
	]
	search_fields = [
		'name',
		'notes',
	]
