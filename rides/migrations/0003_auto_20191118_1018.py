# Generated by Django 2.2.5 on 2019-11-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_profile_rides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]