from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PendingPayments
from .serializers import PaymentSerializer

@api_view(["GET"])
def payments_get(request) :
    pending_payments = PendingPayments.objects.all()
    payment_serializer = PaymentSerializer(pending_payments, many=True)
    return Response(payment_serializer.data)