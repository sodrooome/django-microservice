# nosql models for database

from django.db import models


class Poll(models.Model):
    vote = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
