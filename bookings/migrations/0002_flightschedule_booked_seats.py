# Generated by Django 4.2.3 on 2024-05-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightschedule',
            name='booked_seats',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
