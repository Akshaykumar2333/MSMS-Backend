# Generated by Django 5.0.6 on 2024-07-09 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Description',
        ),
        migrations.DeleteModel(
            name='Diet',
        ),
        migrations.DeleteModel(
            name='Medication',
        ),
        migrations.DeleteModel(
            name='Precaution',
        ),
        migrations.DeleteModel(
            name='SymptomDescription',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]
