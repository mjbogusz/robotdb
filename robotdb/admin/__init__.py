from django.contrib import admin

from .ApplicationAdmin import ApplicationAdmin
from .ArticleAdmin import ArticleAdmin
from .FeatureAdmin import FeatureAdmin
from .MobileBaseAdmin import MobileBaseAdmin
from .ProjectAdmin import ProjectAdmin
from .RobotAdmin import RobotAdmin

from robotdb.models import Application, Article, Feature, MobileBase, Project, Robot

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(MobileBase, MobileBaseAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Robot, RobotAdmin)
