# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import requests
# Create your views here.


from textblob import TextBlob
from .forms import BlobTextForm


def django_view(request, text):
    # get the response from the URL
    testimonial = TextBlob(text)

    response = testimonial.sentiment.polarity
    return HttpResponse(response)

def polarity_view(request):
	if request.method == 'POST':
		formdata = TextBlob(request.POST)
		text = fromdata.cleaned_data['blobtext']
		testimonial = TextBlob(text)
		response = testimonial.sentiment.polarity
		return HttpResponse(response)
