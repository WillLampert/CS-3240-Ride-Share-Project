# Generated by Django 2.2.5 on 2019-12-01 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0010_profile_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='hometown',
        ),
    ]