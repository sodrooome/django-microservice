from rest_framework import generics
from .serializers import PollSerializer
from .models import Poll


# basic API view
# doesnt work if want to fetching a data
# from another services
class PollAPIView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
