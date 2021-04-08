# Generated by Django 3.1.7 on 2021-03-16 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20210316_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='faculty_name',
        ),
        migrations.AddField(
            model_name='student_link',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]