# Generated by Django 3.1.5 on 2021-03-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0012_auto_20210319_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
