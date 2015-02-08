from rest_framework import serializers

from .models import Business
from .models import Offer


class BusinessSerializer(serializers.ModelSerializer):
	lng = serializers.FloatField(source='long')
	class Meta:
		model = Business
		fields = ('id', 'name', 'description', 'lat', 'lng', 'google_place_id', 'category')

class OfferSerializer(serializers.ModelSerializer):
	business = BusinessSerializer()

	class Meta:
		model = Offer
		fields = ('id', 'valid_to', 'business', 'title', 'description')
