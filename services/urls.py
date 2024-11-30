from django.urls import path
from . import views

from django.shortcuts import render

def success_page(request):
    return render(request, 'services/success.html')


urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('error/', views.error_page, name='error_page'),
    path('success/', views.success_page, name='success_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
