from django.shortcuts import render, get_object_or_404, redirect
from event.models import event
from .models import booking
from django.contrib import messages




def bookings(request):
    if request.method =="POST":
        event_id = request.POST['event_id']
        user_id = request.POST['user_id']
        event_title = request.POST['event_title']
        name = request.POST['name']
        email =  request.POST['mail']
        
        phone = request.POST['phone']
        ticket = request.POST['ticket']
        date = request.POST['date']

        has_booked = booking.objects.all().filter(event_id=event_id,user_id=user_id)
        if has_booked:
            messages.error(request,"You have already make a booking of this sport")
            return redirect('/booking/'+event_id)
        book = booking(email=email,event_id=event_id,user_id=user_id,event_title=event_title,name=name,phone=phone,ticket=ticket,date=date)
        book.save()

        messages.success(request,"You Booking has Recived")
        return redirect('/booking/'+event_id)







def book(request,booking_id):
    events = get_object_or_404(event,pk=booking_id)
    context = {
        'event':events
    }

    return render(request,'booking/booking.html',context)