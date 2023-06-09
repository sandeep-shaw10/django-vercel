# Generated by Django 4.2.1 on 2023-05-10 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('role', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('links', models.URLField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False, verbose_name='Working Currently')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_link', models.URLField(default='', help_text='Use 1:1 image for better results', verbose_name='Image Link')),
                ('occupation', models.CharField(max_length=255, verbose_name='Display Occupation')),
                ('country', models.CharField(max_length=255)),
                ('banner_text', models.TextField(verbose_name='Banner Text')),
                ('resume_link', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('twitter_link', models.URLField(verbose_name='Twitter Link')),
                ('github_link', models.URLField(verbose_name='Github Link')),
                ('linkedin_link', models.URLField(verbose_name='LinkedIn Link')),
            ],
            options={
                'verbose_name': 'Personal Information',
                'verbose_name_plural': 'Personal Information',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('image_link', models.URLField()),
                ('description', models.TextField()),
                ('project_link', models.URLField()),
                ('tags', models.CharField(help_text='Separate tags with "," and First 3 tag will be considered ', max_length=100)),
                ('is_archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('percentage', models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
