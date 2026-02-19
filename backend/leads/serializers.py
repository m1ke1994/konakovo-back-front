from decimal import Decimal

from django.db.models import Min
from rest_framework import serializers

from core.models import Service

from .models import DayScenario, Lead, ScenarioItem, ServiceRequest


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ("name", "contact", "message")


class ScenarioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioItem
        fields = ("title", "price", "quantity")


class DayScenarioSerializer(serializers.ModelSerializer):
    items = ScenarioItemSerializer(many=True)

    class Meta:
        model = DayScenario
        fields = (
            "name",
            "contact",
            "date",
            "guests_count",
            "comment",
            "total_price",
            "items",
        )

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        scenario = DayScenario.objects.create(**validated_data)
        ScenarioItem.objects.bulk_create(
            [ScenarioItem(scenario=scenario, **item_data) for item_data in items_data]
        )
        return scenario


class ServiceRequestSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=False, min_value=1, write_only=True, default=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ServiceRequest
        fields = (
            "name",
            "contact",
            "service_title",
            "service_slug",
            "price",
            "total_price",
            "quantity",
            "message",
            "preferred_date",
        )
        read_only_fields = ("service_title", "price", "total_price")

    def create(self, validated_data):
        service_slug = validated_data.get("service_slug", "")
        service = Service.objects.filter(slug=service_slug).first()
        if service is None:
            raise serializers.ValidationError({"service_slug": "Услуга не найдена."})

        quantity = validated_data.pop("quantity", 1)
        raw_price = getattr(service, "price", None)
        if raw_price is None:
            raw_price = service.tariffs.aggregate(min_price=Min("price")).get("min_price")
        if raw_price is None:
            raise serializers.ValidationError({"service_slug": "Для услуги не задана стоимость."})

        price = Decimal(raw_price)
        validated_data["service_title"] = service.title
        validated_data["service_slug"] = service.slug
        validated_data["price"] = price
        validated_data["total_price"] = price * Decimal(quantity)
        return super().create(validated_data)
