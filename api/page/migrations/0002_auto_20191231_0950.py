# Generated by Django 2.2.6 on 2019-12-31 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='np',
            name='Title',
            field=models.CharField(max_length=120),
        ),
    ]
