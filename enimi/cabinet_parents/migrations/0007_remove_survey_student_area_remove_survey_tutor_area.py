# Generated by Django 4.1.4 on 2023-01-03 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_parents', '0006_studentarea_survey_tutorarea_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='student_area',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='tutor_area',
        ),
    ]
