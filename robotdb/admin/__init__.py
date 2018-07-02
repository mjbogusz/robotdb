from django.contrib import admin

from .RobotAdmin import RobotAdmin
from .ApplicationAdmin import ApplicationAdmin
from .ArticleAdmin import ArticleAdmin
from .FeatureAdmin import FeatureAdmin
from .ProjectAdmin import ProjectAdmin

from robotdb.models import Application, Article, Feature, Project, Robot

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Robot, RobotAdmin)
