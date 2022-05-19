# Generated by Django 4.0.4 on 2022-05-19 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCourse', '0008_alter_course_timecreated_alter_course_timemodified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='correlative',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCourse.subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppCourse.course'),
        ),
    ]