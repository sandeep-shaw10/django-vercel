from django.utils.html import format_html
from django.core.validators import MaxValueValidator
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


class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    about = models.TextField()
    links = models.URLField(null=True, blank=True)
    is_current = models.BooleanField(default=False, verbose_name='Working Currently')

    def __str__(self):
        return self.role
    
    def work(self):
        return f'{self.role}, {self.company}'
    
    work.short_description = 'Position'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveSmallIntegerField(default=0, blank=True, null=True, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image_link = models.URLField()
    description = models.TextField()
    project_link = models.URLField()
    tags = models.CharField(max_length=100, help_text='Separate tags with "," and First 3 tag will be considered ')
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image_link:
            return format_html('<img src="{}" width="192px"/>'.format(self.image_link))
        else:
            return ''
    
    image_tag.short_description = 'Image'