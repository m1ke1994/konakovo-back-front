from django.contrib import admin

from .models import DayScenario, Lead, ScenarioItem, ServiceRequest


@admin.action(description="Отметить как обработанные")
def mark_as_processed(modeladmin, request, queryset):
    queryset.update(is_processed=True)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "is_processed", "created_at")
    list_filter = ("is_processed", "created_at")
    search_fields = ("name", "contact", "message")
    ordering = ("-created_at",)
    actions = (mark_as_processed,)


class ScenarioItemInline(admin.TabularInline):
    model = ScenarioItem
    extra = 0


@admin.register(DayScenario)
class DayScenarioAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "date", "total_price", "is_processed", "created_at")
    list_filter = ("is_processed", "date", "created_at")
    search_fields = ("name", "contact", "comment")
    ordering = ("-created_at",)
    inlines = (ScenarioItemInline,)
    actions = (mark_as_processed,)


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "service_title", "preferred_date", "is_processed", "created_at")
    list_filter = ("is_processed", "preferred_date", "created_at")
    search_fields = ("name", "contact", "service_title", "service_slug", "message")
    ordering = ("-created_at",)
    actions = (mark_as_processed,)
