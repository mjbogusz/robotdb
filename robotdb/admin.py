from django import forms
from django.contrib import admin
from robotdb.models import Application, Article, Feature, Project, Robot, RobotFeature, RobotImage

class RobotFeatureInline(admin.TabularInline):
	model = RobotFeature
	extra = 1

class RobotImageInline(admin.TabularInline):
	model = RobotImage
	extra = 1
	exclude = ('thumbnail', 'width', 'height',)

class RobotAdminForm(forms.ModelForm):
	notes = forms.CharField(widget = forms.Textarea, required = False)

	class Meta:
		model = Robot
		exclude = ()

class RobotAdmin(admin.ModelAdmin):
	form = RobotAdminForm
	inlines = (RobotFeatureInline, RobotImageInline, )
	filter_horizontal = ('applications', 'articles', 'projects',)

class FeatureAdmin(admin.ModelAdmin):
	inlines = (RobotFeatureInline, )

class RobotImageAdmin(admin.ModelAdmin):
	exclude = ('height', 'width',)

admin.site.register(Application)
admin.site.register(Article)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Project)
admin.site.register(Robot, RobotAdmin)
admin.site.register(RobotImage, RobotImageAdmin)
