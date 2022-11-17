from django.urls import re_path
from .views import HomeView

urlspatterns = [
    path('', HomeView.as_view(), name='home' )
]