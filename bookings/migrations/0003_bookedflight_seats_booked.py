# Generated by Django 4.2.3 on 2024-05-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_flightschedule_booked_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedflight',
            name='seats_booked',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
