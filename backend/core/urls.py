from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import HeroBlockAPIView, ReviewViewSet

router = DefaultRouter()
router.register("reviews", ReviewViewSet, basename="reviews")

urlpatterns = [
    path("hero/", HeroBlockAPIView.as_view(), name="hero-api"),
    path("", include(router.urls)),
]
