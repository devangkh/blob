# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import requests, json
# Create your views here.

import gensim
import re
from bs4 import BeautifulSoup
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
            rawtext = form_data.data['blobtext']
            cleantext = BeautifulSoup(rawtext, "lxml").text
            text = re.sub('"', '', cleantext)
            summary = gensim.summarization.summarizer.summarize(text, ratio=0.2, word_count=None, split=False)
            altered_response=HttpResponse(summary)
            altered_response["Access-Control-Allow-Origin"] = "*"
            return altered_response
        except Exception as e:
            form_data = BlobTextForm(request.POST)
            rawtext = form_data.data['blobtext']
            cleantext = BeautifulSoup(rawtext, "lxml").text
            text = re.sub('"', '', cleantext)
            altered_response=HttpResponse(text)
            altered_response["Access-Control-Allow-Origin"] = "*"
            return altered_response
        
@csrf_exempt
def keywords_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        rawtext = form_data.data['blobtext']
        cleantext = BeautifulSoup(rawtext, "lxml").text
        text = re.sub('"', '', cleantext)
        keywords = get_ranked_phrases(text)
        altered_response=HttpResponse(keywords)
        altered_response["Access-Control-Allow-Origin"] = "*"
        return altered_response


@csrf_exempt
def keywordsScore_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        rawtext = form_data.data['blobtext']
        cleantext = BeautifulSoup(rawtext, "lxml").text
        text = re.sub('"', '', cleantext)
        keywords = get_ranked_phrases(text, True)
        altered_response=HttpResponse(keywords)
        altered_response["Access-Control-Allow-Origin"] = "*"
        return altered_response
    
@csrf_exempt
def wordFrequency_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        rawtext = form_data.data['blobtext']
        cleantext = BeautifulSoup(rawtext, "lxml").text
        text = re.sub('"', '', cleantext)
        wordfre = get_word_frequency_distribution(text)
        j = json.dumps(wordfre)
        return HttpResponse(j)
    
@csrf_exempt
def wordDegrees_view(request):
    if request.method == 'POST':
        form_data = BlobTextForm(request.POST)
        rawtext = form_data.data['blobtext']
        cleantext = BeautifulSoup(rawtext, "lxml").text
        text = re.sub('"', '', cleantext)
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
    
    
    
    
    
    
    
