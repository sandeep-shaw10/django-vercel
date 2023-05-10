from django.contrib import admin
from .models import PersonalData, Experience, Skill, Project


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'occupation')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('work', 'start_date', 'end_date')
    list_filter = ['start_date']

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
    list_filter = ['percentage']
    search_fields=['name']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image_tag')
    list_filter = ['is_archived']
    search_fields=['title', 'description']

admin.site.register(PersonalData, PersonalDataAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)