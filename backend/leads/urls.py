from django.urls import path

from .views import DayScenarioCreateAPIView, LeadCreateAPIView, ServiceRequestCreateAPIView

urlpatterns = [
    path("leads/", LeadCreateAPIView.as_view(), name="lead-create"),
    path("day-scenarios/", DayScenarioCreateAPIView.as_view(), name="day-scenario-create"),
    path("service-requests/", ServiceRequestCreateAPIView.as_view(), name="service-request-create"),
]
