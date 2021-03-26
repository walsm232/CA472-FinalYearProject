# Generated by Django 3.1.5 on 2021-02-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0005_userprofile_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account_type',
            field=models.CharField(choices=[('Student', 'Student'), ('Tutor', 'Tutor')], default='Student', max_length=20),
        ),
    ]
