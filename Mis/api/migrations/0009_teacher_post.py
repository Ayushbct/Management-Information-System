# Generated by Django 4.2.4 on 2023-12-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_routine_teacher_alter_routine_time_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='post',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]