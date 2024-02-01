# global level library import
import json

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Book
from .models import Author

@csrf_exempt
# Create your views here.
def singular(request):
    if request.method == "GET":
        '''
        PURPOSE:

        STEPS:
        1. get book id from query params
        2. use book id to get object from db
        3. serialise the book object
        4. return a HTTP response
        '''
        book_id = request.GET.get("id", "")
        book = Book.objects.get(pk=book_id)
        book_json_response = serializers.serialize("json", [book])
        return HttpResponse(book_json_response, headers={
            "content-type": "application/json"
        })
    elif request.method == "POST":
        """
        PURPOSE:
        STEPS:
        1. Get the book data from HTTP Request body
        2. Deserialize the book data to a Python dictionary
        3. Get the values of the attributes for the Book object from the dictionary
        4. Save the Book object using those values
        5. Return a success HTTP Response
        """
        book_data = json.loads(request.body)
        author = Author()
        author_string = book_data.get("author")
        if author_string.__contains__(" "):
            author_array = author_string.split()
            author.first_name = author_array[0]
            author.last_name = author_array[1]
        else:
            author.first_name = author_string

        book = Book()
        book.title = book_data.get("title")
        book.author = author
        book.summary = book_data.get("summary")
        book.isbn = book_data.get("isbn")
        # book.genre.add(book_data.get("genre"))
        return HttpResponse("This book has been created")
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
        book_id = request.GET.get("id", "")
        book = Book.objects.get(pk=book_id)
        book_data = json.loads(request.body)
        book_complete = ["title", "author", "summary", "isbn", "genre"]
        book_data_set = set(book_data)
        book_comp_set = set(book_complete)
        if book_data_set.intersection(book_comp_set):
            for attr in book_data:
                book.attr = book_data.get("f{attr}")
        else:
            book.title = book_data.get("title")
            book.author = book_data.get("author")
            book.summary = book_data.get("summary")
            book.isbn = book_data.get("isbn")
            book.genre = book_data.get("genre")
        return HttpResponse("This book has been updated")
    elif request.method == "DELETE":
        """
        PURPOSE:
        to delete a book object from project's Django db

        STEPS:
        1. get book id from query params
        2. use book id to get object from db
        3. delete the book object
        4. return the HTTP response
        """
        book_id = request.GET.get("id", "")
        old_book = Book.objects.get(pk=book_id)
        old_book.delete()
        return HttpResponse("The book has been deleted")

@csrf_exempt
def list(request):
    if(request.method == "GET"):
        '''
        PURPOSE:

        STEPS:
        1. get all book objects
        2. serialise objects
        3. return them as HTTP response
        '''
        book_list = Book.objects.all()
        json_list = serializers.serialize("json", book_list)
        return HttpResponse(json_list, headers={
            "content-type": "application/json"
        })
    elif(request.method == "DELETE"):
        """
        PURPOSE:

        STEPS:
        1. get all book objects
        2. delete all book objects
        3. return `success` HTTP response
        """
        black_list = Book.objects.all()
        black_list.delete()
        return HttpResponse("The book list has been deleted")