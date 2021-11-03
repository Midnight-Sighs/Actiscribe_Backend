# Generated by Django 3.2.8 on 2021-11-03 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actiscribe', '0003_resident_last_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='note_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resident',
            name='last_assessment',
            field=models.DateField(),
        ),
    ]