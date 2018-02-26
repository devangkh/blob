# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import requests, json
# Create your views here.

import gensim
import re
from textblob import TextBlob
from .forms import BlobTextForm, DualTextForm
from django.views.decorators.csrf import csrf_exempt
from blob.rake import *
from blob.scapy import *


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
		altered_response=HttpResponse(response)
                altered_response["Access-Control-Allow-Origin"] = "*"
                return altered_response

@csrf_exempt
def summary_view(request):
	if request.method == 'POST':
            try:
		form_data = BlobTextForm(request.POST)
		text = form_data.data['blobtext']
		text = re.sub('"', '', text)
		summary = gensim.summarization.summarizer.summarize(text, ratio=0.2, word_count=None, split=False)
		return HttpResponse(summary)
            except Exception as e:
                form_data = BlobTextForm(request.POST)
                text = form_data.data['blobtext']
                text = re.sub('"', '', text)
                return HttpResponse(text)
        
@csrf_exempt
def keywords_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        text = form_data.data['blobtext']
        text = re.sub('"', '', text)
        keywords = get_ranked_phrases(text)
        return HttpResponse(keywords)


@csrf_exempt
def keywordsScore_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        text = form_data.data['blobtext']
        text = re.sub('"', '', text)
        keywords = get_ranked_phrases(text, True)
        return HttpResponse(keywords)
    
@csrf_exempt
def wordFrequency_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        text = form_data.data['blobtext']
        text = re.sub('"', '', text)
        wordfre = get_word_frequency_distribution(text)
        j = json.dumps(wordfre)
        return HttpResponse(j)
    
@csrf_exempt
def wordDegrees_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        text = form_data.data['blobtext']
        text = re.sub('"', '', text)
        wordfre = get_word_degrees(text)
        j = json.dumps(wordfre)
        return HttpResponse(j)
    
@csrf_exempt
def similarity_view(request):
    if request.method == 'POST':
        form_data = DualTextForm(request.POST)
        text1 = form_data.data['base']
        ref = form_data.data['ref']
        text = re.sub('"', '', text1)
        ref = re.sub('"', '', ref)
        similarity_score = similarity(text, ref)
        j = json.dumps(similarity_score)
        return HttpResponse(j)
    
    
    
    
    
    
    
