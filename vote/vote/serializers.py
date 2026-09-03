import requests
from django.conf import settings
from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

    def validate_question_id(self, value):
        try:
            response = requests.get(
                f"{settings.QUESTION_SERVICE_URL}/question/{value}",
                timeout=5,
            )
        except requests.RequestException as exc:
            raise serializers.ValidationError(
                "question service is unreachable"
            ) from exc
        if response.status_code != 200:
            raise serializers.ValidationError("question does not exist")
        return value
