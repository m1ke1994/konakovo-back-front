from django.urls import path

from .views import DayScenarioCreateAPIView, LeadCreateAPIView

urlpatterns = [
    path("leads/", LeadCreateAPIView.as_view(), name="lead-create"),
    path("day-scenarios/", DayScenarioCreateAPIView.as_view(), name="day-scenario-create"),
]
