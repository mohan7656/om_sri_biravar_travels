from django.db import models

# Create your models here.
class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    passenger = models.IntegerField()

    def __str__(self):
        return self.full_name