# Generated by Django 4.2.5 on 2023-12-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0061_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='department',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
