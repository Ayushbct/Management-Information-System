# Generated by Django 4.1.13 on 2024-03-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_teacher_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='note',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
