from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializer import ShelterSerializer
from .models import Cats_data
# Create your views here.
class ShelterView(ListAPIView):
    queryset = Cats_data.objects.all()
    serializer_class = ShelterSerializer

class ShelterDetailsView(RetrieveAPIView):
    queryset = Cats_data.objects.all()
    serializer_class = ShelterSerializer
