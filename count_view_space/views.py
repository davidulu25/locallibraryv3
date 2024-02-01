import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from bookinstance_model_space.models import BookInstance

