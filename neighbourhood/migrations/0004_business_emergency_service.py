# Generated by Django 3.1.2 on 2020-11-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_auto_20201101_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='emergency_service',
            field=models.BooleanField(default=False),
        ),
    ]