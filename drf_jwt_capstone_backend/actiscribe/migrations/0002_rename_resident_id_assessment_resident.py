# Generated by Django 3.2.8 on 2021-11-03 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actiscribe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='resident_id',
            new_name='resident',
        ),
    ]
