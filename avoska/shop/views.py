from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, OrderForm
from .models import Order_table, Status, User_table, Product, Role

# Create your views here.

def mainpage(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            default_role = get_object_or_404(Role, name='user')
            user.id_role = default_role
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Перенаправить, если пользователь уже вошел

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Ошибка авторизации. Проверьте имя пользователя и пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    orders = Order_table.objects.filter(id_user=request.user)
    return render(request, 'dashboard.html', {'orders': orders})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.id_user = request.user
            default_status = Status.objects.get(code='new')
            new_request.id_status = default_status
            new_request.order_date = form.cleaned_data.get('order_date')
            new_request.delivery_address = form.cleaned_data.get('delivery_address')
            new_request.save()
            return redirect('dashboard')
    else:
        form = OrderForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, 'У вас недостаточно прав для доступа к этой странице')
        return render(request, 'admin_panel.html')
    
    if request.user.is_superuser:
        if request.method == 'POST':
            order_id = request.POST.get('order_id')
            new_status_id = request.POST.get('status')
            
            if order_id and new_status_id:
                order = get_object_or_404(Order_table, id=order_id)
                new_status = get_object_or_404(Status, id=new_status_id)
                order.id_status = new_status
                order.save()
                messages.success(request, f'Статус заказа #{order.id} успешно обновлён.')
            else:
                messages.error(request, 'Возникла ошибка при обновлении')
                
    orders = Order_table.objects.all()
    statuses = Status.objects.all()
    
    return render(request, 'admin_panel.html', {'orders': orders, 'statuses': statuses})