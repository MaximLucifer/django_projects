from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, RequestForm
from .models import CleaningRequest

# Create your views here.

def base(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'clining.auth_backend.cliningAuthBackend'
            login(request, user, backend='clining.auth_backend.cliningAuthBackend')
            return redirect('dashboard')
    else:
            form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password, backend='clining.auth_backend.cliningAuthBackend')
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            error_message = "Неверный логин или пароль. Попробуйте снова"
    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    requests = CleaningRequest.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'requests': requests})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user
            new_request.save()
            return redirect('/dashboard')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, 'У вас недостаточно прав для доступа к этой странице')
    requests = CleaningRequest.objects.all()
    return render(request, 'admin.html', {'requests': requests})