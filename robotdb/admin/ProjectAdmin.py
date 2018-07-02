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
			'year',
			'link',
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
		'notes',
	]
