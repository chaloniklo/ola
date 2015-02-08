from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from datetime import datetime

from com.models import Booking
from com.serializers import BookingSerializer
from com.serializers import BookingListSerializer

from django.db.models import Max

from biz.models import Business
from biz.serializers import Offer

from biz.models import Offer
from biz.serializers import OfferSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def booking_element(request, id):
	try:
		bk = Booking.objects.get(id=id)
	except Booking.DoesNotExist:
		raise Http404

	if request.method == 'GET':
		serializer = BookingListSerializer(bk)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = BookingSerializer(bk, data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		bk.delete()
        return Response(status.HTTP_200_OK)	

@api_view(['GET', 'POST', 'PUT'])
def booking_list(request):
	if request.method == 'GET':
		bs = Booking.objects.filter(coupon_availed=False)
		serializer = BookingListSerializer(bs, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = BookingSerializer(data=request.data)
		if (serializer.is_valid()):
			serializer.save(time=datetime.now())
			return Response(data={'status': "OK"}, status=status.HTTP_201_CREATED)
		return Response(data={'status' : "FAIL"}, status=status.HTTP_400_BAD_REQUEST)	
	elif request.method == 'PUT':
		bk = Booking.objects.latest('id')
		serializer = BookingSerializer(bk, data=request.data)
		if (serializer.is_valid()):
			serializer.save()
			return Response(data={'status' : "OK"})
		return Response(data={'status' : "FAIL"}, status=status.HTTP_400_BAD_REQUEST)	


@api_view(['GET'])
def offer_list(request, id):
	if request.method == 'GET':
		try:
			bk = Booking.objects.get(id=id)
		except Booking.DoesNotExist:
			raise Http404

		bs = Offer.objects.filter(business=Business.objects.filter(category=bk.category))
		serializer = OfferSerializer(bs, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def offer_list_latest(request):
	if request.method == 'GET':
		try:
			bk = Booking.objects.latest('id')
		except Booking.DoesNotExist:
			raise Http404

		bs = Offer.objects.filter(business=Business.objects.filter(category=bk.category))
		serializer = OfferSerializer(bs, many=True)
		return Response({'status' : "OK", "response" : serializer.data})

@api_view(['GET'])
def coupon_list(request):
	if request.method == 'GET':
		bs = Booking.objects.filter(coupon_availed=False, offer_selected__isnull=False)
		serializer = BookingListSerializer(bs, many=True)
		return Response({'status' : "OK", "response" : serializer.data})

