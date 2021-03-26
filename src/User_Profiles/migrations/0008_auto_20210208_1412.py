# Generated by Django 3.1.5 on 2021-02-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0007_auto_20210208_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='availability',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='experience',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='defaultprofilepicture.png', upload_to='profilepictures/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qualifications',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='topics',
            field=models.TextField(max_length=500),
        ),
    ]
