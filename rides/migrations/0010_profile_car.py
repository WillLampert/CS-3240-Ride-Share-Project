# Generated by Django 2.2.5 on 2019-12-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0009_auto_20191201_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='car',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
