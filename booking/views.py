from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking

#home page
def home(request):
    return render(request,'home.html')

#services page
def services(request):
    return render(request,'services.html')

#contact page
def contact(request):
    return render(request,'contact.html')

#about us page
def about_us(request):
    return render(request,'about_us.html')

#booking
def booking(request):
    return render(request,'booking.html')

#booking_form
def booking_form(request):
    if request.method == "POST":
        Booking.objects.create(
            full_name=request.POST.get("full_name"),
            mobile_number=request.POST.get("mobile_number"),
            email=request.POST.get("email"),
            pickup_location=request.POST.get("pickup_location"),
            drop_location=request.POST.get("drop_location"),
            pickup_date=request.POST.get("pickup_date"),
            pickup_time=request.POST.get("pickup_time"),
            passenger=request.POST.get("passenger"),
        )

        return render(request, "success.html")

    return render(request, "booking.html")