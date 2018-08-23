from django.contrib import admin
from robotdb.models import RobotEquipment

class RobotEquipmentInline(admin.TabularInline):
	model = RobotEquipment
	extra = 1
