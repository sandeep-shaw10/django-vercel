from django.contrib import admin
from .models import PersonalData, Experience


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'occupation')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('work', 'start_date', 'end_date')
    list_filter = [('start_date')]


admin.site.register(PersonalData, PersonalDataAdmin)
admin.site.register(Experience, ExperienceAdmin)