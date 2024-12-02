from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

def home(request):
    return render(request, 'home.html', {'show_cookie_banner': not request.session.get('cookie_acknowledged', False)})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save booking to DB
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})