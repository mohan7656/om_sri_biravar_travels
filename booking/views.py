from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

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
    if request.method=="POST":
        print("view called")
        full_name = request.POST.get("full_name")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        pickup_location = request.POST.get("pickup_location")
        drop_location = request.POST.get("drop_location")
        pickup_date = request.POST.get("pickup_date")
        pickup_time = request.POST.get("pickup_time")
        passenger = request.POST.get("passenger")
        print(request.POST)
        try:
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Dev@0610#7",
                database = "osbt_db"
            )

            cursor = conn.cursor()

            query = """
            INSERT INTO booking(full_name,mobile_number,email,pickup_location,drop_location,pickup_date,pickup_time,passenger)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = (
                full_name,
                mobile_number,
                email,
                pickup_location,
                drop_location,
                pickup_date,
                pickup_time,
                passenger
            )
            cursor.execute(query,values)
            conn.commit()
            print("booking inserted successfully")

            cursor.close()
            conn.close()

            return render(request,'success.html')
        except Exception as e:
            print("mysql error:", e)
    return render(request,'booking.html')