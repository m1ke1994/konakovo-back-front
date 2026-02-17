from rest_framework import serializers

from .models import Article, HeroBlock, News, Review, Service, Tariff


class HeroBlockSerializer(serializers.ModelSerializer):
    background_image = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = HeroBlock
        fields = ("id", "title", "description", "background_image", "avatar")

    def _absolute_url(self, media_field):
        if not media_field:
            return None
        request = self.context.get("request")
        if request is None:
            return media_field.url
        return request.build_absolute_uri(media_field.url)

    def get_background_image(self, obj):
        return self._absolute_url(obj.background_image)

    def get_avatar(self, obj):
        return self._absolute_url(obj.avatar)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "title",
            "slug",
            "preview_image",
            "preview_description",
            "content_type",
            "published_date",
            "created_at",
        )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "slug", "description", "image", "published_date")


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ("id", "title", "slug", "description", "duration", "price", "order")


class ServiceSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    tariffs = TariffSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "is_category",
            "order",
            "children",
            "tariffs",
        )

    def get_children(self, obj):
        children = obj.children.all().order_by("order")
        return ServiceSerializer(children, many=True, context=self.context).data
