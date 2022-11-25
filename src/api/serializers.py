from rest_framework import serializers
from user.models import User_details

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User_details
        fields = "__all__"