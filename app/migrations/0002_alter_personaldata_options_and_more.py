# Generated by Django 4.2.1 on 2023-05-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldata',
            options={'verbose_name': 'Personal Information', 'verbose_name_plural': 'Personal Information'},
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='banner_text',
            field=models.TextField(verbose_name='Banner Text'),
        ),
    ]
