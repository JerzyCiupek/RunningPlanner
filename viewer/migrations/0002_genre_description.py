# Generated by Django 4.1.1 on 2022-09-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
