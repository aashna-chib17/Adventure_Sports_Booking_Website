from django.shortcuts import render,redirect
from booking.models import booking
from django.contrib.auth.models import User
from django.contrib import messages





def mybooking(request):

        bookings = booking.objects.all().filter(user_id = request.user.id)
        context = {
        'bookings':bookings,
        }


        return render(request,'booking/mybooking.html',context)
def remove(request):
        if request.method =="POST":
                event_id = request.POST['event']
                booking.objects.all().filter(pk = event_id).delete()
                messages.success(request,"Your Booking has been Cancelled")
                return redirect('mybooking')


