"""defines url PATTERNS FOR U users"""

from django.urls import path, include
from .import views

app_name = 'users'
urlpatterns = [
    # Include default auth URLs
    path('', include('django.contrib.auth.urls')),

    # Registration page.
    path('register/', views.register, name='register'),
]
