from django.contrib import admin
from django.utils.html import format_html

from .models import Article, HeroBlock, Review


@admin.register(HeroBlock)
class HeroBlockAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)
    fields = (
        "title",
        "description",
        "background_image",
        "background_image_preview",
        "avatar",
        "avatar_preview",
        "is_active",
    )
    readonly_fields = ("background_image_preview", "avatar_preview")

    def has_add_permission(self, request):
        if HeroBlock.objects.exists():
            return False
        return super().has_add_permission(request)

    @admin.display(description="Превью фона")
    def background_image_preview(self, obj):
        if obj and obj.background_image:
            return format_html(
                '<img src="{}" style="max-width: 320px; border-radius: 8px;" />',
                obj.background_image.url,
            )
        return "Изображение не загружено"

    @admin.display(description="Превью аватара")
    def avatar_preview(self, obj):
        if obj and obj.avatar:
            return format_html(
                '<img src="{}" style="max-width: 140px; border-radius: 9999px;" />',
                obj.avatar.url,
            )
        return "Изображение не загружено"


admin.site.site_header = "Администрирование"
admin.site.site_title = "Админ-панель"
admin.site.index_title = "Управление контентом"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("avatar", "name", "event_name", "rating", "date", "created_at")
    list_filter = ("rating", "date")
    search_fields = ("name", "event_name")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "content_type", "is_published", "published_date", "created_at")
    list_filter = ("content_type", "is_published", "published_date")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Основное", {"fields": ("title", "slug", "content_type", "is_published", "published_date")}),
        ("Превью", {"fields": ("preview_image", "preview_description")}),
        ("Контент", {"fields": ("content", "video_url")}),
    )
