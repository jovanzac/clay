from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Appointment
from .serializers import AppointmentsSerializer

@api_view(["GET"])
def appointments_get(request) :
    users = Appointment.objects.all()
    serializer = AppointmentsSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def appointments_post(request) :
    serializer = AppointmentsSerializer(data=request.data)
    if serializer.is_valid() :
        serializer.save()
    
    return Response(serializer.data)