from django.contrib import admin
from .models import Application, Article, Feature, Project, Robot, RobotImage

admin.site.register(Application)
admin.site.register(Article)
admin.site.register(Feature)
admin.site.register(Project)
admin.site.register(Robot)
admin.site.register(RobotImage)
