# Generated by Django 4.1.5 on 2023-01-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0002_response_cabinet_tutor_alter_response_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='hello_message',
            field=models.TextField(default='Здравствуйте. Меня заинтересовала ваша анкета!', max_length=3000, verbose_name='Приветственное сообщение'),
        ),
    ]
