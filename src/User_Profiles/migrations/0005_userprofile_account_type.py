# Generated by Django 3.1.5 on 2021-02-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0004_auto_20210128_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='account_type',
            field=models.CharField(default='Student', max_length=20),
        ),
    ]
