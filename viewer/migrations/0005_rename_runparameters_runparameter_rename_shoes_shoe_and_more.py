# Generated by Django 4.1.1 on 2022-09-21 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_runparameters_distance_runparameters_pulse_avg_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RunParameters',
            new_name='RunParameter',
        ),
        migrations.RenameModel(
            old_name='Shoes',
            new_name='Shoe',
        ),
        migrations.RenameField(
            model_name='runparameter',
            old_name='shoes',
            new_name='shoe',
        ),
        migrations.RenameField(
            model_name='shoe',
            old_name='shoes_model',
            new_name='shoe_model',
        ),
    ]