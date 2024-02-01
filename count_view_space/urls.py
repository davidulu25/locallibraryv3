from django.urls import path
from . import views

urlpatterns = [
    path('bookinstance/filter/', name="count_books"),
]