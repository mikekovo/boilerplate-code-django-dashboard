# Generated by Django 3.2.6 on 2021-10-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_profile', '0003_profile_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]