import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Author

@csrf_exempt
def singular(request):
    if request.method == "GET":
        """
        PURPOSE:

        STEPS:
        1. get author id from query param
        2. use auhtorid to get author object from db
        3. serialise the object
        4. return a HTTP response
        """

        author_id = request.GET.get("id", "")
        author =  Author.objects.get(pk=author_id)
        author_get_response = serializers.serialize("json", [author])
        return HttpResponse(author_get_response, headers={
            "content-type": "application/json"
        })
    elif request.method == "POST":
        """
        PURPOSE:

        STEPS:
        1. get author information from the HTTP request
        2. deserialise author data to a Python dictionary
        3. get the values of the Author object from the dictionary
        4. save the author object with the derived attributes
        5. return a success HTTP response
        """
        author_data = json.loads(request.body)

        author = Author()
        author.first_name = author_data.get("first_name")
        author.last_name = author_data.get("last_name")
        return HttpResponse("Author has been created")
    elif request.method == "PATCH":
        """
        PURPOSE:
        to modify an existing book's data

        STEPS:
        1. get the data from the request body
        2. check what field(s) need(s) to be changed
        3. make changes
        4. return success HTTP response
        """
        author_id = request.GET.get("id", "")
        author = Author.objects.get(pk=author_id)
        author_data = json.loads(request.body)
        author_complete = ["first_name", "last_name", "date_of_birth", "date_of_death"]
        author_data_set = set(author_data)
        author_comp_set = set(author_complete)
        if author_data_set.intersection(author_comp_set):
            for attr in author_data:
                author.attr = author_data.get("f{attr}")
        else:
            author = Author.objects.create(first_name=f"{author_data.get("first_name")}", last_name=f"{author_data.get("last_name")}", date_of_birth=f"{author_data.get("date_of_birth")}", date_of_death=f"{author_data.get("date_of_death")}")
        return HttpResponse("This author has been updated")
    elif request.method == "DELETE":
        pass

@csrf_exempt
def list(request):
    if request.method == "GET":
        pass
    elif request.method == "PATCH":
        pass
    elif request.method == "DELETE":
        pass