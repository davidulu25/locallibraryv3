from django.urls import path
from . import views

urlpatterns = [
    path('singular/', views.singular, name="book_singular"),
    path('list/', views.list, name="book_list"),
]
