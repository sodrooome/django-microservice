from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    # MongoDB primary keys are ObjectIds: DRF's auto-generated id field
    # assumes an integer PK and errors serializing them, so make it explicit
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Question
        fields = ("id", "questions", "pub_date", "pub_update")
