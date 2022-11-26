from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PastSurgeries, PastAppointments
from .serializers import SurgeriesSerializer, AppointmentsSerializer

@api_view(["GET"])
def p_appointments(request) :
    appointments = PastAppointments.objects.all()
    serializer = AppointmentsSerializer(appointments, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def p_surgeries(request) :
    surgeries = PastSurgeries.objects.all()
    serializer = SurgeriesSerializer(surgeries, many=True)
    return Response(serializer.data)