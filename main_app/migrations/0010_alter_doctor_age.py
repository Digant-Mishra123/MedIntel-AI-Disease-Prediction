# Generated by Django 5.1.6 on 2025-03-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_doctor_dob_remove_patient_dob_doctor_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(default=15),
        ),
    ]
