# Generated by Django 5.1 on 2024-09-30 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sultan', '0005_remove_project_description_remove_project_tittle'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PROJECT',
        ),
    ]
