# Generated by Django 3.2.16 on 2023-04-06 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_navigationmenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardmenu',
            name='has_been_modified',
        ),
        migrations.RemoveField(
            model_name='dashboardmenu',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='navigationmenu',
            name='has_been_modified',
        ),
        migrations.RemoveField(
            model_name='navigationmenu',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='sidemenu',
            name='has_been_modified',
        ),
        migrations.RemoveField(
            model_name='sidemenu',
            name='last_modified',
        ),
    ]
