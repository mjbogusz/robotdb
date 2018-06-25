from django.contrib import admin
from robotdb.models import Application, Article, Feature, Project, Robot, RobotFeature, RobotImage

class RobotFeatureInline(admin.TabularInline):
	model = RobotFeature
	extra = 1

class RobotAdmin(admin.ModelAdmin):
	inlines = (RobotFeatureInline, )

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
