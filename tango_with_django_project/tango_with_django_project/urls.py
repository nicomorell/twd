from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from rango import views
# DJANGO CONF allows us access to the variables defined within our projects settings.py file
from django.conf import settings

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/rango/'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)
# Construct a dictionary to pass to the template engine as its context.
if settings.DEBUG:
    urlpatterns+= patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
