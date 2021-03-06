# Generated by Django 4.0.4 on 2022-05-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCourse', '0005_alter_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enddate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='shortname',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='startdate',
            field=models.DateTimeField(null=True),
        ),
    ]
