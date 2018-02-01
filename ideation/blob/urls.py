from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url

from .views import django_view, polarity_view


urlpatterns = [
    url(r'^sentiment/polarity_word/(?P<text>[-\w]+)$', django_view,),
    url(r'^sentiment/polarity/$', polarity_view,),
]
