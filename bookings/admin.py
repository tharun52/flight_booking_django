from django.contrib import admin
from .models import FlightSchedule, BookedFlight

# Register your models here
admin.site.register(FlightSchedule)
admin.site.register(BookedFlight)
