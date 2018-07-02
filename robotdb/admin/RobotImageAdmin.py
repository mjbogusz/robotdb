from django.contrib import admin
from robotdb.models import RobotImage

class RobotImageInline(admin.TabularInline):
	model = RobotImage
	extra = 1
	exclude = ('thumbnail', 'width', 'height',)
