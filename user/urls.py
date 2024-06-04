from django.urls import path
from .views import home, register, user_login

app_name='user'
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
