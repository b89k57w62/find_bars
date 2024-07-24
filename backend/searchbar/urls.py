from django.urls import path
from .views import PlacesAPIView

urlpatterns = [
    path('places/', PlacesAPIView.as_view(), name='places_api'),
]
