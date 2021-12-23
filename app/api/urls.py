from django.urls import path, include
from .views import firstFunction

urlpatterns = [
    path('first', firstFunction)
]
