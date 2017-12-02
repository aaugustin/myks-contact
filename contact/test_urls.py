from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('contact.urls', namespace='contact')),
]
