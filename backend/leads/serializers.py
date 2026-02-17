from rest_framework import serializers

from .models import DayScenario, Lead, ScenarioItem


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
