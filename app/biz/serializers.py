from rest_framework import serializers

from .models import Business
from .models import Offer


class BusinessSerializer(serializers.ModelSerializer):
	class Meta:
		model = Business

class OfferSerializer(serializers.ModelSerializer):
	business = BusinessSerializer()

	class Meta:
		model = Offer
		fields = ('id', 'valid_to', 'business', 'title', 'description')
