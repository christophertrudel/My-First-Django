from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	# (r'^my_first_django/', include('my_first_django.foo.urls')),
	(r'^polls/$', 'polls.views.index'),
	(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
	(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
	(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
	
	# Uncomment the next two lines to enable the admin and the admin/doc respectivly:
	(r'^admin/', include(admin.site.urls)),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)