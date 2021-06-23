from django.urls import path, include
from . import views

urlpatterns = [
    path('newsearch/', views.new_search, name='new_search'),
    ]