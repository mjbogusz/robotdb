from django.contrib import admin
from robotdb.models import RobotFeature

class RobotFeatureInline(admin.TabularInline):
	model = RobotFeature
	extra = 1
