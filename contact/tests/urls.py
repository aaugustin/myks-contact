from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^', include('contact.urls', namespace='contact', app_name='contact')),
)
