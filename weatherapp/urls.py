from django.urls import path
from .views import home_view
from .views import signup_view,signin_view,signout_view,weather_view


urlpatterns = [
    path('',home_view,name='home'),
    path('signup/',signup_view,name='signup'),
    path('signin/',signin_view,name='signin'),
    path('signout/',signout_view,name='signout'),
    path('weather/',weather_view,name='weather')
]
