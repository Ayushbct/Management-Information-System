# Generated by Django 4.2.4 on 2023-12-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_profile_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='teacher',
        ),
        migrations.AddField(
            model_name='routine',
            name='teacher',
            field=models.ManyToManyField(to='api.teacher'),
        ),
    ]
