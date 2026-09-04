from django.db import models


class Question(models.Model):
    questions = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.questions
