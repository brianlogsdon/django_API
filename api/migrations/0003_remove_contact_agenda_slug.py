# Generated by Django 2.1.1 on 2019-01-13 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190113_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='agenda_slug',
        ),
    ]
