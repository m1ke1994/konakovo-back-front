from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import DayScenario, Lead, ServiceRequest
from .serializers import DayScenarioSerializer, LeadSerializer, ServiceRequestSerializer


class LeadCreateAPIView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class DayScenarioCreateAPIView(generics.CreateAPIView):
    queryset = DayScenario.objects.all()
    serializer_class = DayScenarioSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class ServiceRequestCreateAPIView(generics.CreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
