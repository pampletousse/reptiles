# Generated by Django 2.2.9 on 2020-01-18 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reptiles_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reptile',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]