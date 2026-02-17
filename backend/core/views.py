from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, HeroBlock, Review
from .serializers import (
    ArticleListSerializer,
    ArticleSerializer,
    HeroBlockSerializer,
    ReviewSerializer,
)


class HeroBlockAPIView(APIView):
    def get(self, request):
        hero = HeroBlock.objects.filter(is_active=True).order_by("-created_at").first()
        if hero is None:
            return Response(
                {"detail": "Активный Hero-блок не найден."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = HeroBlockSerializer(hero, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.filter(is_published=True)
    serializer_class = ArticleListSerializer


class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.filter(is_published=True)
    serializer_class = ArticleSerializer
    lookup_field = "slug"
