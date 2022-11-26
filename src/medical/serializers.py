from rest_framework import serializers
from .models import UserVitals, PastAppointments, PastSurgeries

class VitalsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserVitals
        fields = "__all__"
        
class AppointmentsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PastAppointments
        fields = "__all__"
        
class SurgeriesSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PastSurgeries
        fields = "__all__"