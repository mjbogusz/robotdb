from django import forms
from django.contrib import admin

from robotdb.models import Application

class ApplicationAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Application
		exclude = ()

class ApplicationAdmin(admin.ModelAdmin):
	form = ApplicationAdminForm
	fieldsets = [
		(None, {'fields': [
			'name',
		]}),
		('Properties', {'fields': [
			'mobility',
			'selfreliantCare',
			'interpersonalInteraction',
			'other',
		]}),
		('Notes', {'fields': [
			'notes',
		]}),
	]

	list_display = [
		'name',
		'mobility',
		'selfreliantCare',
		'interpersonalInteraction',
		'other',
	]
	list_filter = [
		'mobility',
		'selfreliantCare',
		'interpersonalInteraction',
		'other',
	]
	search_fields = [
		'name',
		'notes',
	]
