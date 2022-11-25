from django.db import models

class Hospitals(models.Model) :
    name = models.CharField(max_length=50)
    contact_number = models.PositiveSmallIntegerField()
    address = models.TextField()
    
    def __str__(self) -> str:
        return self.name