# Generated by Django 3.1.5 on 2021-01-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='Add a bio to tell other students about yourself', max_length=500),
        ),
    ]
