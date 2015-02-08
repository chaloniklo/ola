from django.conf.urls import patterns, include, url
from django.contrib import admin

from pax import views as pax_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^booking/$', pax_views.booking_list),
	url(r'^booking/(?P<id>[0-9]+)$', pax_views.booking_element),

	url(r'^offer/(?P<id>[0-9]+)$', pax_views.offer_list),
	url(r'^offer/$', pax_views.offer_list_latest),

	url(r'^coupon/$', pax_views.coupon_list),

    url(r'^admin/', include(admin.site.urls)),
)
