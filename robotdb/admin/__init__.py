from django.contrib import admin

from .ArticleAdmin import ArticleAdmin
from .FeatureAdmin import FeatureAdmin
from .MobileBaseAdmin import MobileBaseAdmin
from .ProjectAdmin import ProjectAdmin
from .RobotAdmin import RobotAdmin
from .SkillAdmin import SkillAdmin

from robotdb.models import Article, Feature, MobileBase, Project, Robot, Skill

admin.site.register(Article, ArticleAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(MobileBase, MobileBaseAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(Skill, SkillAdmin)
