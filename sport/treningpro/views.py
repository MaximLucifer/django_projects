from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from .forms import RegistrationForm, BookingForm
from .models import Booking, Booking_status, Payment_method, Role, User_role, User, Training_type 

# Create your views here.

def mainpage(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Неправильный логин или пароль')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user_id=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user_id = request.user
            default_status = get_object_or_404(Booking_status, code='pending')
            new_request.booking_status = default_status
            new_request.save()
            return redirect('dashboard')
    else:
        form = BookingForm()
    return render(request, 'create_request.html', {'form': form})

@staff_member_required
def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, 'У вас недостаточно прав')
        return render(request, 'admin_panel.html')
    
    if request.user.is_superuser:
        booking_id = request.POST.get('booking_id')
        new_status_id = request.POST.get('booking_status')
        
        if booking_id and new_status_id:
            booking = get_object_or_404(Booking, id=booking_id)
            new_status = get_object_or_404(Booking_status, id=new_status_id)
            booking.status_id = new_status
            booking.save()
            messages.success(request, f'Статус бронирования #{booking.id} успешно изменён')
        else:
            messages.error(request, 'Возникла ошибка при обновлении')
    
    bookings = Booking.objects.all()
    statuses = Booking_status.objects.all()
    
    return render(request, 'admin_panel.html', {'bookings': bookings, 'statuses': statuses})