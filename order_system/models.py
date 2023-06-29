from django.db import models
from django.contrib.auth.models import User

# from cloudinary.models import CloudinaryField

# Booking Model

class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
