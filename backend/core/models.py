from django.db import models
from django.utils.text import slugify


class HeroBlock(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Имя",
        default="Лиза Стручкова",
    )
    description = models.TextField(
        verbose_name="Описание",
        default="Делюсь событиями, тишиной и тёплыми практиками в Конаково.",
    )
    background_image = models.ImageField(
        upload_to="hero/background/",
        verbose_name="Фоновое изображение",
    )
    avatar = models.ImageField(
        upload_to="hero/avatar/",
        verbose_name="Аватар",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        verbose_name = "Hero-блок"
        verbose_name_plural = "Hero-блок"

    def __str__(self):
        return self.title


class Review(models.Model):
    class RatingChoices(models.IntegerChoices):
        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    avatar = models.ImageField(upload_to="reviews/", null=True, blank=True)
    name = models.CharField(max_length=255)
    event_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices)
    text = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.name} ({self.event_name})"


class Article(models.Model):
    class ContentTypeChoices(models.TextChoices):
        ARTICLE = "article", "Статья"
        VIDEO = "video", "Видео"

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    preview_image = models.ImageField(upload_to="articles/", null=True, blank=True)
    preview_description = models.TextField()
    content = models.TextField()
    content_type = models.CharField(max_length=20, choices=ContentTypeChoices.choices)
    video_url = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    published_date = models.DateField(verbose_name="Дата публикации")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Статья / Видео"
        verbose_name_plural = "Статьи и видео"
        ordering = ["-published_date", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or "article"
            slug = base_slug
            index = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{index}"
                index += 1
            self.slug = slug
        super().save(*args, **kwargs)
