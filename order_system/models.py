from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# from cloudinary.models import CloudinaryField

# Booking Model
BOOKING_OPTIONS = (
    ("17:00", "17:00"),
    ("17:30", "17:30"),
    ("18:00", "18:00"),
    ("18:30", "18:30"),
    ("19:00", "19:00"),
    ("19:30", "19:30"),
    ("20:00", "20:00"),
    ("20:30", "20:30"),
    ("21:00", "21:00"),
    ("21:30", "21:30"),
    ("22:00", "22:00"),
    ("22:30", "22:30") ,
)

class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=BOOKING_OPTIONS, default="17:00")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['created_on']

# Pulled from Django tutorial blog specified in README.
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
