from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_places_data
from.serializers import PlaceSerializer
import requests

class PlacesAPIView(APIView):
    def get(self, request, format=None):
        query = "bar"
        district = request.query_params.get("district", None)
        location = "23.6978,120.9605"  # Taiwan
        if district:
            geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
            geocode_params = {
                "address": district,
                "key": settings.GOOGLE_PLACES_API_KEY
            }
            geocode_response = requests.get(geocode_url, params=geocode_params)
            if geocode_response.status_code == 200:
                geocode_data = geocode_response.json()
                if geocode_data["results"]:
                    location = geocode_data['results'][0]['geometry']['location']
                    location = f"{location['lat']},{location['lng']}"
        
        radius = request.query_params.get("radius", 1000)

        places_data = fetch_places_data(query, location, radius)
        if places_data and "results" in places_data:
            serializer = PlaceSerializer(data=places_data["results"], many=True)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Failed to fetch data"}, status=status.HTTP_400_BAD_REQUEST)