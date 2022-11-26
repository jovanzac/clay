from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User_details
from .serializers import UserSerializer
from medical.models import UserVitals
from medical.serializers import VitalsSerializer

@api_view(["GET"])
def dashboard_get(request) :
    users = User_details.objects.all()
    user_serializer = UserSerializer(users, many=True)
    user_vitals = UserVitals.objects.all()
    vitals_serializer = VitalsSerializer(user_vitals, many=True)
    data = {
        "user_data" : user_serializer.data,
        "medical_data" : vitals_serializer.data,
    }
    return Response(data)