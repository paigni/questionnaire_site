# Generated by Django 4.1.2 on 2022-10-26 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_rename_time_create_question_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
    ]