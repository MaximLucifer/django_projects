from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, RequestForm
from .models import CleaningRequest

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_page = request.GET.get('next', '/module2/dashboard/')  # если next не указан, перенаправим на default
            return redirect(next_page)
    else:
        form = RegistrationForm()
    return render(request, 'module2/register.html', {'form': form})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Попробуем аутентифицировать через оба бэкенда
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next', '/module2/dashboard/')
            return redirect(next_page)
        else:
            error_message = "Неверный логин или пароль. Попробуйте снова."

    return render(request, 'module2/login.html', {'error_message': error_message})

@login_required(login_url='/module2/login/')
def dashboard(request):
    requests = CleaningRequest.objects.filter(user=request.user)
    return render(request, 'module2/dashboard.html', {'requests': requests})

@login_required(login_url='/module2/login/')
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('module2_dashboard')
    else:
        form = RequestForm()
    return render(request, 'module2/create_request.html', {'form': form})

@login_required(login_url='/module2/login/')
def admin_panel(request):
    if not request.user.is_superuser:
        return redirect('module2_login')
    requests = CleaningRequest.objects.all()
    return render(request, 'module2/admin.html', {'requests': requests})
