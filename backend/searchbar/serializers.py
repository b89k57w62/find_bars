from rest_framework import serializers

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField()
    vicinity = serializers.CharField()
    place_id = serializers.CharField()
    latitude = serializers.FloatField(source='geometry.location.lat', required=False)
    longitude = serializers.FloatField(source='geometry.location.lng', required=False)
