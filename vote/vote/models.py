from django.db import models


class Vote(models.Model):
    # The question lives in the separate question service's own database,
    # so it's referenced by id (validated over HTTP, see serializers.py)
    # rather than a cross-service ForeignKey, which can't work here.
    question_id = models.CharField(max_length=24)
    date_updated = models.DateTimeField(auto_now_add=True)
