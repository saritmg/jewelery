# Generated by Django 2.2.6 on 2019-12-19 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
    ]
