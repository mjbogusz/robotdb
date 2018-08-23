from django import forms
from django.contrib import admin

from robotdb.models import Skill

class SkillAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Skill
		exclude = ()

class SkillAdmin(admin.ModelAdmin):
	form = SkillAdminForm
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
