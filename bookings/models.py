from django.db import models
from django.contrib.auth.models import User

class FlightSchedule(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    take_off_timing = models.DateTimeField()
    max_seats = models.PositiveIntegerField()
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    booked_seats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.source} to {self.destination} - {self.take_off_timing.strftime('%Y-%m-%d %H:%M')}"

class BookedFlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight_schedule = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    seats_booked = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.flight_schedule.source} to {self.flight_schedule.destination}"
