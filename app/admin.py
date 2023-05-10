from django.contrib import admin
from .models import PersonalData


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'occupation')


admin.site.register(PersonalData,PersonalDataAdmin)