from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template.response import TemplateResponse
import datetime
import random
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError  

def create_review(request):
    return render(request, "reviews/create_review.html")
