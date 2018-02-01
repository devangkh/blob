from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url



urlpatterns = [
    url(r'^sentiment/polarity/(?P<text>[-\w]+)$', django_view,),
]
