# Generated by Django 3.1.2 on 2020-11-02 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0008_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nhoodz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood'),
            preserve_default=False,
        ),
    ]
