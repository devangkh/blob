# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import requests
# Create your views here.


from textblob import TextBlob


def django_view(request, text):
    # get the response from the URL
    testimonial = TextBlob(text)

    response = testimonial.sentiment.polarity
    return HttpResponse(response)