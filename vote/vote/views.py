from rest_framework import generics
from .serializers import VoteSerializer
from .models import Vote


class VoteAPIView(generics.ListCreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
