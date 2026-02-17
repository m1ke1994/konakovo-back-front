from rest_framework import serializers

from .models import HeroBlock, Review


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
