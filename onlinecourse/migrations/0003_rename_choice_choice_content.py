# Generated by Django 4.2.3 on 2024-09-01 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='content',
        ),
    ]
