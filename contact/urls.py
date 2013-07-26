from django.conf.urls import patterns, url

urlpatterns = patterns('contact.views',
    url(r'^$', 'contact', name='form'),
    url(r'^thanks/$', 'thanks', name='thanks'),
)
