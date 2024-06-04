# Flight Booking System using Django

This is a small flight booking system built using Django. It allows users to view available flights, book flights, and manage their bookings. Admins can manage flight schedules, including creating, updating, and deleting schedules.

## Features

### User Functionality
- List available flights within a specified time frame
- Book flights with passenger details
- View and cancel upcoming flights

### Admin Functionality
- Create flight schedules
- Update schedule details
- Delete schedules

## Models

### FlightSchedule
- `source` (CharField): The departure location.
- `destination` (CharField): The arrival location.
- `take_off_timing` (DateTimeField): The date and time of departure.
- `maximum_seats` (IntegerField): The total number of seats available.
- `pricing` (DecimalField): The price of the flight.
- `booked_seats` (IntegerField, default=0): The number of seats already booked.

### BookedFlight
- `user` (ForeignKey): The user who booked the flight.
- `flight_schedule` (ForeignKey): The flight schedule being booked.
- `booking_time` (DateTimeField): The date and time of booking.
- `seats_booked` (IntegerField): The number of seats booked.

## Views

- `display_available_flights`: Display available flights.
- `book_flight`: Book a flight.
- `confirm_booking`: Confirm a flight booking.
- `view_booked_flights`: View booked flights.
- `cancel_booking`: Cancel a booking (requires user confirmation).

## Running the Project

To run the project, execute the following command:

```sh
python manage.py runserver
