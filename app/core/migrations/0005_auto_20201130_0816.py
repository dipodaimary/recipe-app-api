# Generated by Django 3.1.3 on 2020-11-30 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='uesr',
            new_name='user',
        ),
    ]
