from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^sentiment/polarity_word/(?P<text>[-\w]+)$', django_view,),
    url(r'^sentiment/polarity$', polarity_view,),
    url(r'^summary$', summary_view,),   
    url(r'^keywordscore$', keywordsScore_view,),
    url(r'^keyword$', keywords_view,),
    url(r'^wordfrequency$', wordFrequency_view,),
    url(r'^worddegree$', wordDegrees_view,),
    url(r'^similarity$', similarity_view,),
]
