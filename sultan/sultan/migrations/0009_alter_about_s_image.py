# Generated by Django 5.1 on 2024-10-01 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sultan', '0008_about_s_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='S_image',
            field=models.ImageField(upload_to='myimages/'),
        ),
    ]
