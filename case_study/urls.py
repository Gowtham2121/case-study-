from django.contrib import admin
from django.urls import path, include
from services import views  # Import views from your services app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('error/', views.error_page, name='error_page'),
    path('success/', views.success_page, name='success_page'),
    path('services/', include('services.urls')),  # Includes your services app URLs
    path('', views.home_page, name='home_page'),  # Route for the root URL
]