# Generated by Django 5.0.2 on 2024-02-22 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrainingProgram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainingprogram',
            old_name='end_date',
            new_name='end_of_registration',
        ),
        migrations.RenameField(
            model_name='trainingprogram',
            old_name='start_date',
            new_name='join_date',
        ),
    ]
