# Generated by Django 4.2.3 on 2023-07-18 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_course_department_subjectstudent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='type',
            field=models.CharField(choices=[('1', 'Present'), ('0.5', 'Late'), ('0', 'Absent')], max_length=250),
        ),
    ]
