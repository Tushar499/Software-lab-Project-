# Generated by Django 4.2.5 on 2023-12-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_alter_task_assessment_alter_task_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assessment',
            field=models.FileField(blank=True, default='', upload_to='uploads'),
        ),
    ]
