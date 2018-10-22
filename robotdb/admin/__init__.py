from django.contrib import admin

from .ArticleAdmin import ArticleAdmin
from .EquipmentAdmin import EquipmentAdmin
from .ProjectAdmin import ProjectAdmin
from .RobotAdmin import RobotAdmin
from .SkillAdmin import SkillAdmin

from robotdb.models import Article, Equipment, Project, Robot, Skill

admin.site.register(Article, ArticleAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Robot, RobotAdmin)
admin.site.register(Skill, SkillAdmin)
