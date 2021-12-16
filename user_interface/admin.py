from django.contrib import admin

from .models import User,InformationModel,EducationModel,ExprienceModel,ProjectModel,SkillSetModel,MessageModel

# Register your models here.

admin.site.register(User)
admin.site.register(InformationModel)
admin.site.register(EducationModel)
admin.site.register(ExprienceModel)
admin.site.register(ProjectModel)
admin.site.register(SkillSetModel)
admin.site.register(MessageModel)
