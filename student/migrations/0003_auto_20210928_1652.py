# Generated by Django 3.1 on 2021-09-28 11:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_stu_question_stuexam_db_sturesults_db'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student_Info',
            new_name='StudentInfo',
        ),
        migrations.AlterModelOptions(
            name='studentinfo',
            options={},
        ),
    ]
