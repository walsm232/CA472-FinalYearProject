# Generated by Django 3.1.5 on 2021-03-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0013_auto_20210319_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='Add a bio to tell others about yourself', max_length=500),
        ),
    ]
