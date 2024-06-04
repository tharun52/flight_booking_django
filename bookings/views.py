from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import FlightSchedule, BookedFlight
from django.db.models import Sum
from django.db.models import Q

@login_required
def search_flights(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        source = request.POST.get('source')
        destination = request.POST.get('destination')

        # Start building the query based on provided criteria
        query = Q(take_off_timing__gt=timezone.now())
        if from_date:
            query &= Q(take_off_timing__date__gte=from_date)
        if to_date:
            query &= Q(take_off_timing__date__lte=to_date)
        if source:
            query &= Q(source__icontains=source)
        if destination:
            query &= Q(destination__icontains=destination)

        # Filter flights based on user input
        flights = FlightSchedule.objects.filter(query)
        available_flights = [flight for flight in flights if flight.booked_seats < flight.max_seats]

        return render(request, 'bookings/available_flights.html', {'flights': available_flights})
    else:
        available_sources = FlightSchedule.objects.values_list('source', flat=True).distinct()
        available_destinations = FlightSchedule.objects.values_list('destination', flat=True).distinct()

        return render(request, 'bookings/search.html', {
            'available_sources': available_sources,
            'available_destinations': available_destinations,
        })

@login_required
def available_flights(request):
    now = timezone.now()
    flights = FlightSchedule.objects.filter(take_off_timing__gt=now)
    available_flights = [flight for flight in flights if flight.booked_seats < flight.max_seats]
    return render(request, 'bookings/available_flights.html', {'flights': available_flights})

@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(FlightSchedule, id=flight_id)
    if request.method == 'POST':
        seats = int(request.POST['seats'])
        if flight.booked_seats + seats <= flight.max_seats:
            flight.booked_seats += seats
            flight.save()
            BookedFlight.objects.create(user=request.user, flight_schedule=flight, seats_booked=seats)
            return redirect('bookings:confirmation', flight_id=flight.id, seats=seats)
    return render(request, 'bookings/book_flight.html', {'flight': flight})

@login_required
def confirmation(request, flight_id, seats):
    flight = get_object_or_404(FlightSchedule, id=flight_id)
    total_price = flight.pricing * int(seats)
    return render(request, 'bookings/confirmation.html', {'flight': flight, 'seats': seats, 'total_price': total_price})

@login_required
def booked_flights(request):
    bookings = BookedFlight.objects.filter(user=request.user)
    return render(request, 'bookings/booked_flights.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(BookedFlight, id=booking_id)
    flight = booking.flight_schedule
    if request.method == 'POST':
        # Check if the user confirmed the cancellation
        if 'confirm_cancel' in request.POST:
            flight.booked_seats -= booking.seats_booked
            flight.save()
            booking.delete()
            return redirect('bookings:available_flights')
        else:
            return redirect('bookings:booked_flights')  # Redirect to booked flights page without cancellation
    return render(request, 'bookings/cancel_booking.html', {'booking': booking})