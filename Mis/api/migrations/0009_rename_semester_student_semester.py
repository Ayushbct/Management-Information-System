# Generated by Django 4.2.3 on 2023-07-16 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_student_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Semester',
            new_name='semester',
        ),
    ]
