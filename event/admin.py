from django.contrib import admin
from .models import event



class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title','city','place','price','is_open')
    list_display_links = ('id','title')
    list_filter = ('city',)
    list_editable = ('is_open', )
    search_fields = ('title','city','place',)

admin.site.register(event,EventAdmin)
