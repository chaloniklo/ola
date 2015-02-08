from django.contrib import admin

from com.models import Booking
from biz.models import Offer
from biz.models import Category
from biz.models import Business

admin.site.register(Booking)
admin.site.register(Business)
admin.site.register(Offer)
admin.site.register(Category)
# Register your models here.
