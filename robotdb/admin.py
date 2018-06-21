from django.contrib import admin
from .models import Robot
from .models import RobotImage

admin.site.register(Robot)
admin.site.register(RobotImage)
