from rest_framework import serializers

from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ("vote", "category")
