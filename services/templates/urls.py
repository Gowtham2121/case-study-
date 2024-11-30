from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('submitted/', views.request_submitted, name='request_submitted'),
    path('track/', views.track_requests, name='track_requests'),
]
