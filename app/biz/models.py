from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length = 15, blank = False, null = False)
	def __unicode__(self):
		return '[%d] %s' % (self.id, self.name)

class Business(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length = 30, blank = False, null = False)
	description = models.CharField(max_length = 100, blank = True, null = True)
	lat = models.FloatField(null=True, blank=True)
	long = models.FloatField(null=True, blank=True)
	google_place_id = models.CharField(max_length = 30, blank = True, null = True)
	category = models.ForeignKey(Category, related_name='businesses', blank=False, null=False)
	def __unicode__(self):
		return '[%d] %s' % (self.id, self.name)


class Offer(models.Model):
	business = models.ForeignKey(Business, related_name='offers')
	valid_to = models.DateTimeField(blank = True, null = True)
	title = models.CharField(max_length = 30, blank=True, null=True)
	description = models.CharField(max_length = 100, blank = True, null = True)
	selected_count = models.IntegerField(blank = False)
	availed_count = models.IntegerField(blank = False)
	def __unicode__(self):
		return '[%d] %s' % (self.id, self.title)


