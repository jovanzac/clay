from django.urls import path
from . import views

urlpatterns = [
    path("appointments/", views.appointments_get),
]
