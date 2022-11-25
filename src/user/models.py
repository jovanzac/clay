from django.db import models
from django.core.exceptions import ValidationError
from healthcare_centres.models import Hospitals

class User_details(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    emergency_contact = models.PositiveIntegerField()
    contact_number = models.PositiveIntegerField()
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=1, choices=(
                                            ("m", "m"),
                                            ("f", "f"))
                           )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    healthcare_centres = models.ManyToManyField(Hospitals)

    def __str__(self) -> str:
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.pk and User_details.objects.exists():
    #         raise ValidationError('There is can be only one User_details instance')
    #     return super(User_details, self).save(*args, **kwargs)