# Generated by Django 2.2 on 2020-08-01 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bock',
            old_name='Email',
            new_name='email',
        ),
    ]
