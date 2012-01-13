from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.forms import AuthenticationForm

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
		(r'^$', 'index.views.home'),
    (r'^', include('lesson.urls')),
)
