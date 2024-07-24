import requests
from django.conf import settings

def fetch_places_data(query, location, radius):
    api_key = settings.GOOGLE_PLACES_API_KEY
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "key": api_key,
        "location": location,
        "radius": radius,
        "keyword": query
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None