from django.urls import path

from .views import SubmitView, ThanksView

app_name = 'contact'

urlpatterns = [
    path(r'', SubmitView.as_view(), name='form'),
    path(r'thanks/', ThanksView.as_view(), name='thanks'),
]
