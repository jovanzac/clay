from django.urls import path
from . import views

urlpatterns = [
    path("history/appointments/", views.p_appointments),
    path("history/surgeries/", views.p_surgeries),
]