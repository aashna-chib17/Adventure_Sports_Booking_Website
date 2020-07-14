from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.mybooking,name="mybooking"),
    path('remove',views.remove,name="delete"),
   
]