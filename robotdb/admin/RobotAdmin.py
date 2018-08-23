from django.contrib import admin
from django import forms

from robotdb.models import Robot
from .RobotEquipmentAdmin import RobotEquipmentInline
from .RobotImageAdmin import RobotImageInline

class RobotAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)
	videoLink = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Robot
		exclude = ()

class RobotAdmin(admin.ModelAdmin):
	form = RobotAdminForm
	inlines = (RobotEquipmentInline, RobotImageInline, )
	filter_horizontal = ('skills', 'articles', 'projects',)
	fieldsets = [
		(None, {'fields': [
			'name',
			'producer',
			'country',
			'year',
			'price',
			'notes',
		]}),
		('Links', {'fields': [
			'link',
			'videoLink',
		]}),
		('Skills', {'fields': [
			'skills',
		]}),
		('Articles', {'fields': [
			'articles',
		]}),
		('Projects', {'fields': [
			'projects',
		]}),
	]

	list_display = [
		'name',
		'producer',
		'country',
		'price',
		'notes',
	]
	list_filter = [
		'producer',
		'country',
		'price',
		'skills',
		'equipment',
	]
	search_fields = [
		'name',
		'producer',
		'notes',
	]
