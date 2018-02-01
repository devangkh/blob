# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import requests
# Create your views here.

import gensim
import re
from textblob import TextBlob
from .forms import BlobTextForm
from django.views.decorators.csrf import csrf_exempt


def django_view(request, text):
    # get the response from the URL
    testimonial = TextBlob(text)

    response = testimonial.sentiment.polarity
    return HttpResponse(response)

@csrf_exempt
def polarity_view(request):
	if request.method == 'POST':
		form_data = BlobTextForm(request.POST)
		text = form_data.data['blobtext']
		testimonial = TextBlob(text)
		response = testimonial.sentiment.polarity
		return HttpResponse(response)

@csrf_exempt
def summary_view(request):
	if request.method == 'POST':
		form_data = BlobTextForm(request.POST)
		text = form_data.data['blobtext']
		text = re.sub('"', '', text)
		summary = gensim.summarization.summarizer.summarize(text, ratio=0.2, word_count=None, split=False)
		return HttpResponse(summary)
