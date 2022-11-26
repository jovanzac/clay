from django.db import models
from user.models import User_details

class PendingPayments(models.Model) :
    hospital_name = models.CharField(max_length=20)
    desc = models.TextField()
    amt = models.IntegerField()
    due_by = models.DateField()

    user_details = models.ForeignKey(
        User_details,
        on_delete=models.CASCADE,
        null=True
    )