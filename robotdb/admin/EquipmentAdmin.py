from django import forms
from django.contrib import admin

from robotdb.models import Equipment

class EquipmentAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Equipment
		exclude = ()

class EquipmentAdmin(admin.ModelAdmin):
	form = EquipmentAdminForm
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
