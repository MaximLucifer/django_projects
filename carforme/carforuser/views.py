from turtle import back
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import RegistrationForm, BookingForm, EmailLoginForm
from .models import Booking, Status, User, Car, Role

# Create your views here.

def mainpage(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            default_role = get_object_or_404(Role, name='Пользователь')
            user.role = default_role
            user.backend = 'carforuser.EmailAuthBackend'
            login(request, user, backend='carforuser.EmailAuthBackend')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

class CustomEmailLoginView(View):
    template_name = 'login.html'
    
    def get(self, request):
        form = EmailLoginForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = EmailLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = request.POST.get['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Неверный адрес электронной почты или пароль')
        else:
            messages.error(request, 'Исправьте ошибки формы')
            
        return render(request, self.template_name, {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login.html')

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(id_user=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.id_user = request.user
            try:
                default_status = Status.objects.get(code='new')
            except Status.DoesNotExist:
                return render(request, 'error.html', {'message': 'Статус по умолчанию не найден.'})
            new_booking.id_status = default_status
            new_booking.booking_date = form.cleaned_data['booking_date']
            new_booking.status_comment = form.cleaned_data.get('status_comment', '')
            new_booking.save()
            return redirect('dashboard') 
    else:
        form = BookingForm()
    
    return render(request, 'create_request.html', {'form': form})

@staff_member_required
def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, 'У вас недостаточно прав для доступа к этой странице')
        return render(request, 'admin_panel.html')

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        new_status_id = request.POST.get('status')

        if booking_id and new_status_id:
            try:
                booking = get_object_or_404(Booking, id=booking_id)
                new_status = get_object_or_404(Status, id=new_status_id)
                booking.id_status = new_status
                booking.save()
                messages.success(request, f'Статус бронирования #{booking.id} успешно обновлён.')
            except Exception as e:
                messages.error(request, f'Ошибка при обновлении: {str(e)}')
        else:
            messages.error(request, 'Пожалуйста, выберите бронирование и статус.')
            
    bookings = Booking.objects.all()
    statuses = Status.objects.all()

    return render(request, 'admin_panel.html', {'bookings': bookings, 'statuses': statuses})