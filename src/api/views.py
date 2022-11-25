from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User_details
from .serializers import UserSerializer

@api_view(["GET"])
def dashboard_get(request) :
    users = User_details.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)