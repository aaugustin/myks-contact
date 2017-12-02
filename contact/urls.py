from django.conf.urls import url

from .views import SubmitView, ThanksView

app_name = 'contact'

urlpatterns = [
    url(r'^$', SubmitView.as_view(), name='form'),
    url(r'^thanks/$', ThanksView.as_view(), name='thanks'),
]
