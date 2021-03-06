# Generated by Django 4.0.4 on 2022-06-28 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0001_squashed_0006_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'user_type': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='customUser_giver', to=settings.AUTH_USER_MODEL),
        ),
    ]
