# Generated by Django 5.1 on 2024-09-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABOUT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Name', models.CharField(max_length=250)),
                ('Age', models.CharField(max_length=520)),
                ('Occupation', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=500)),
                ('Email', models.CharField(max_length=500)),
                ('Nationality', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CONTACT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EDUCATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Degree', models.CharField(max_length=250)),
                ('Department', models.CharField(max_length=250)),
                ('Institute', models.CharField(max_length=250)),
                ('Session', models.CharField(max_length=250)),
                ('History', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EXPERIENCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Position', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=250)),
                ('Time', models.CharField(max_length=250)),
                ('Representation', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FUNFACT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Experience_year', models.CharField(max_length=250)),
                ('Client_count', models.CharField(max_length=250)),
                ('Project_count', models.CharField(max_length=250)),
                ('Digital_products', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='HOMEPAGE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Article', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PROJECT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Image_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RESARCH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Mention', models.CharField(max_length=500)),
                ('Resarch_name', models.CharField(max_length=250)),
                ('Description', models.CharField(max_length=250)),
                ('Time', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SERVICE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle1web', models.CharField(max_length=100)),
                ('Tittle2security', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SKILL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('HTML_percantage', models.CharField(max_length=250)),
                ('CSS_percantage', models.CharField(max_length=250)),
                ('Python_percantage', models.CharField(max_length=250)),
                ('JavaScript', models.CharField(max_length=250)),
                ('Research', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TESTIMONIAL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Client_name', models.CharField(max_length=250)),
                ('Company_name', models.CharField(max_length=250)),
                ('Articles', models.CharField(max_length=250)),
                ('JavaScript', models.CharField(max_length=250)),
                ('Research', models.CharField(max_length=250)),
            ],
        ),
    ]
