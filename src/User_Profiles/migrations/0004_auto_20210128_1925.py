# Generated by Django 3.1.5 on 2021-01-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0003_auto_20210128_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='defaultprofilepicture.png', upload_to='profilepictures/'),
        ),
    ]