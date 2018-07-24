from django import forms
from django.contrib import admin

from robotdb.models import MobileBase

class MobileBaseAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = MobileBase
		exclude = ()

class MobileBaseAdmin(admin.ModelAdmin):
	form = MobileBaseAdminForm
	fieldsets = [
		(None, {'fields': [
			'name',
		]}),
		('Notes', {'fields': [
			'notes',
		]}),
	]

	list_display = [
		'name',
	]
	search_fields = [
		'name',
		'notes',
	]
