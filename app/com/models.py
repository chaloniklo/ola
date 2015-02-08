from django.db import models
from django.contrib.auth.models import User
from biz.models import Offer
from biz.models import Category

#from django.contrib.gis.db import models
#from django.contrib.gis.geos import GEOSException, GEOSGeometry
#TODO server setup issue forced us to abandon GEOS



class Booking(models.Model):
	user = models.ForeignKey(User, related_name='bookings')
	time = models.DateTimeField(blank = True, null = True)
	src_lat = models.FloatField(null=True, blank=True)
	src_long = models.FloatField(null=True, blank=True)
	dest_lat = models.FloatField(null=True, blank=True)
	dest_long = models.FloatField(null=True, blank=True)
	offer_selected = models.ForeignKey(Offer, related_name='bookings', blank=True, null=True)
	coupon_availed = models.BooleanField(default=False)
	category = models.ForeignKey(Category, related_name='bookings', blank=True, null=True)
	ride_started = models.BooleanField(default=False)
#	src = models.PointField(null=True, blank=True)
#	objects = models.GeoManager()
	def __unicode__(self):
		return '[%d] %s' % (self.id, self.time)


