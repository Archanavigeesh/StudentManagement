# Generated by Django 3.2.7 on 2021-09-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]
