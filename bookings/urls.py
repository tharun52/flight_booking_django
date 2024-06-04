from django.urls import path
from . import views

app_name="bookings"
urlpatterns = [
    path('', views.available_flights, name='available_flights'),
    path('search/', views.search_flights, name='search_flights'), 
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('confirmation/<int:flight_id>/<int:seats>/', views.confirmation, name='confirmation'),
    path('booked_flights/', views.booked_flights, name='booked_flights'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
