from django import forms
from django.contrib import admin

from robotdb.models import Feature
from .RobotFeatureAdmin import RobotFeatureInline

class FeatureAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Feature
		exclude = ()

class FeatureAdmin(admin.ModelAdmin):
	form = FeatureAdminForm
	inlines = (RobotFeatureInline, )
	fieldsets = [
		(None, {'fields': [
			'name',
		]}),
		('Parameters', {'fields': [
			'parameters',
		]}),
		('Notes', {'fields': [
			'notes',
		]}),
	]

	list_display = [
		'name',
		'parameters',
	]
	search_fields = [
		'name',
		'parameters',
		'notes',
	]
