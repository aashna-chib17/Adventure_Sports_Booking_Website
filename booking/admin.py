from django.contrib import admin
from .models import booking

class bookingDisplay(admin.ModelAdmin):
    list_display = ('name','event_id','user_id','event_title')

admin.site.register(booking,bookingDisplay)
    