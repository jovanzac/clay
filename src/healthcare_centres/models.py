from django.db import models
from user.models import User_details

class Hospitals(models.Model) :
    name = models.CharField(max_length=50)
    contact_number = models.PositiveSmallIntegerField()
    address = models.TextField()
    
    user_details = models.ManyToManyField(User_details)
    
    def __str__(self) -> str:
        return self.name