# Generated by Django 4.0.4 on 2022-05-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppActivity', '0001_initial'),
        ('AppCourse', '0003_subject_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='activities',
            field=models.ManyToManyField(blank=True, to='AppActivity.activity'),
        ),
    ]