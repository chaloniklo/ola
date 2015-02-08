from rest_framework import serializers

from .models import Booking
from biz.serializers import OfferSerializer

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking

class BookingListSerializer(serializers.ModelSerializer):
	offer_selected = OfferSerializer()

	class Meta:
		model = Booking
		fields = ('id', 'offer_selected', 'ride_started', 'category')

