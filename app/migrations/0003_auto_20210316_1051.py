# Generated by Django 3.1.7 on 2021-03-16 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='faculty_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='section_id',
        ),
        migrations.CreateModel(
            name='Student_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.section')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
