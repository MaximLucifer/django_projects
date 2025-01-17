from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, TaskForm, EmailLoginForm
from .models import Task, Category, Status, Client

# Create your views here.

def mainpage(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'support.EmailAuthBackend'
            login(request, user, backend='support.EmailAuthBackend')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

class EmailLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = EmailLoginForm

    def form_valid(self, form):
        user = form.get_user()
        return redirect('dashboard')

    def form_invalid(self, form):
        return super().form_invalid(form)
    
def logout_view(request):
    logout(request)
    return redirect('login.html')
    
@login_required
def support_dashboard(request):
    tasks = Task.objects.filter(id_user=request.user)
    return render(request, 'support_dashboard.html', {'tasks': tasks})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.id_user = request.user
            new_task.save()
            return redirect('support_dashboard')
    else:
        form = TaskForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def admin_panel(request):
    if not request.user.is_superuser:
        messages.error(request, 'У вас недостаточно прав для доступа к этой странице.')

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        new_status_id = request.POST.get('status')

    if task_id and new_status_id:
        task = get_object_or_404(Task, id=task_id)
        new_status = get_object_or_404(Status, id=new_status_id)
        task.id_status = new_status
        task.save()
        messages.success(request, f'Статус задачи #{task.id} успешно обновлён')
    else:
        messages.error(request, 'Возникла ошибка при обновлении.')

    tasks = Task.objects.all()

    return render(request, 'admin_panel.html', {'tasks': tasks})
