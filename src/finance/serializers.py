from rest_framework import serializers
from .models import PendingPayments

class PaymentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = PendingPayments
        fields = "__all__"