from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url

from .views import django_view


urlpatterns = [
    url(r'^sentiment/polarity/(?P<text>[-\w]+)$', django_view,),
]
