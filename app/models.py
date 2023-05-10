from django.utils.html import format_html
from django.db import models


class PersonalData(models.Model):
    name = models.CharField(max_length=255)
    image_link = models.URLField(verbose_name='Image Link', default='', help_text = 'Use 1:1 image for better results')
    occupation = models.CharField(max_length=255, verbose_name='Display Occupation')
    country = models.CharField(max_length=255)
    banner_text = models.TextField(verbose_name='Banner Text')
    resume_link = models.URLField()
    email = models.EmailField()
    twitter_link = models.URLField(verbose_name='Twitter Link')
    github_link = models.URLField(verbose_name='Github Link')
    linkedin_link = models.URLField(verbose_name='LinkedIn Link')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"

    def image_tag(self):
        if self.image_link:
            return format_html('<img src="{}" width="192px"/>'.format(self.image_link))
        else:
            return ''
    
    image_tag.short_description = 'Image'