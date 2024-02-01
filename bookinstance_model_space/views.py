import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.query import QuerySet

from .models import Book

def runner(request):
    pass

@csrf_exempt
def singular(request):
    pass