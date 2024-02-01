from django.urls import path
from . import views

urlpatterns = [
    path('singular/', views.singular, name="author_singular"),
    path('list/', views.list, name="author_list"),
]