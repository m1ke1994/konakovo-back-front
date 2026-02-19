from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.name} ({self.contact})"


class DayScenario(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    date = models.DateField()
    guests_count = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Сценарий дня"
        verbose_name_plural = "Сценарии дня"

    def __str__(self):
        return f"{self.name} - {self.date}"


class ScenarioItem(models.Model):
    scenario = models.ForeignKey(
        DayScenario,
        related_name="items",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Элемент сценария"
        verbose_name_plural = "Элементы сценария"

    def __str__(self):
        return self.title


class ServiceRequest(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    service_title = models.CharField(max_length=255)
    service_slug = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    message = models.TextField(blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Заявка на услугу"
        verbose_name_plural = "Заявки на услуги"

    def __str__(self):
        return f"{self.name} - {self.service_title}"
