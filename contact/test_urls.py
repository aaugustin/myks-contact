from django.urls import include, path

urlpatterns = [
    path(r'', include('contact.urls', namespace='contact')),
]
