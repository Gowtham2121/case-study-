from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import Customer

def home_page(request):
    return render(request, 'services/home.html')

def success_page(request):
    return render(request, 'services/success.html')

def error_page(request):
    return render(request, 'services/error.html', {'message': 'An error occurred. Please try again later.'})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)# Automatically log the user in after successful registration
            Customer.objects.create(
                user=user,
                name=user.username,  # Default to username; can be customized
                email=user.email if user.email else ""  # Use the email if provided
            )
            return redirect('submit_request')  # Redirect to the submit request page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('submit_request')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    return render(request, 'registration/login.html')

@login_required
def submit_request(request):
    # Check if the customer exists for the logged-in user
    customer = Customer.objects.filter(user=request.user).first()
    print("Logged-in user:", request.user)  # Debugging: Check the user
    print("Customer found:", customer)  # Debugging: Check the customer object

    if not customer:
        return render(request, 'services/error.html', {'message': 'No customer found. Please add a customer.'})

    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            return redirect('success_page')  # Redirect to success page
    else:
        form = ServiceRequestForm()

    return render(request, 'services/submit_request.html', {'form': form})

def logout_user(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')
