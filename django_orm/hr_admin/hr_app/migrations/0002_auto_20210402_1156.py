# Generated by Django 2.2.4 on 2021-04-02 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
    ]
