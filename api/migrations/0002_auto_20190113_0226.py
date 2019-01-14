# Generated by Django 2.1.1 on 2019-01-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='agenda_slug',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
    ]
