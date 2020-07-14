from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.bookings,name="booking"),
    path('<int:booking_id>',views.book,name="book"),
    
   
]