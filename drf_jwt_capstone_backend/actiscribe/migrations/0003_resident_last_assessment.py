# Generated by Django 3.2.8 on 2021-11-03 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actiscribe', '0002_rename_resident_id_assessment_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='last_assessment',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
