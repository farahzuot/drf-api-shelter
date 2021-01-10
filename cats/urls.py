from django.contrib import admin
from django.urls import path,include

from .views import ShelterDetailsView,ShelterView

urlpatterns = [
    path('', ShelterView.as_view(), name = 'shelterList'),
    path('<int:pk>', ShelterDetailsView.as_view(), name = 'shelterDetails'),
]
