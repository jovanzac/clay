from django.db import models
from user.models import User_details

class UserVitals(models.Model) :
    blood_pressure = models.IntegerField()
    heart_rate = models.IntegerField()
    oxygen_level = models.IntegerField()
    body_temp = models.IntegerField()
    
    user = models.OneToOneField(
        User_details,
        on_delete=models.CASCADE,
        null=True,
    )
    
    

class Components(models.Model) :
    name = models.CharField(max_length=20)
    value = models.IntegerField()
    normal_min = models.IntegerField()
    normal_max = models.IntegerField()
    
    user_vitals = models.ForeignKey(UserVitals, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class PastAppointments(models.Model) :
    hospital = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    diagnosis = models.TextField()
    date = models.DateTimeField()
    prescriptions = models.TextField()
    
    user = models.ForeignKey(User_details, on_delete=models.CASCADE)
    
class PastSurgeries(models.Model) :
    hospital = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    report = models.TextField()
    date = models.DateTimeField()
    
    user = models.ForeignKey(User_details, on_delete=models.CASCADE)