# Generated by Django 3.0 on 2021-03-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210331_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='small_description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='story_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
