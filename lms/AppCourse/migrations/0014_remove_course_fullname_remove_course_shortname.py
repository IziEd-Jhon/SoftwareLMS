# Generated by Django 4.0.4 on 2022-06-01 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCourse', '0013_course_year_alter_course_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='course',
            name='shortname',
        ),
    ]