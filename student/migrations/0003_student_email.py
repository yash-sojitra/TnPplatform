# Generated by Django 5.0.2 on 2024-02-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Email',
            field=models.EmailField(default='ec@aa.asdas', max_length=254),
            preserve_default=False,
        ),
    ]