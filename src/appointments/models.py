from django.db import models
from user.models import User_details

class Appointment(models.Model) :
    hospital = models.CharField(max_length=20)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=20)

    user = models.ForeignKey(
        User_details,
        on_delete=models.CASCADE,
        )