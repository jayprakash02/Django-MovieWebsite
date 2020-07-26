# Generated by Django 3.0.8 on 2020-07-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0005_auto_20200725_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now=True)),
                ('Post', models.ManyToManyField(to='view.Post', verbose_name='Comments')),
            ],
        ),
    ]
