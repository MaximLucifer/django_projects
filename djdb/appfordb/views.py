from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News, Category
from .forms import ProfileForm, CategoryForm, UserRegistrationForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView

# Create your views here.
def base_view(request):
    return render(request, 'base.html')

def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

def news_list(request, category_id=None):
    categories = Category.objects.all()  # Get all categories

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        news = category.news.all()
    else:
        news = News.objects.all()

    return render(request, 'news_list.html', {'news': news, 'categories': categories})

def articles_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = category.news.all()
    return render(request, 'articles_by_category.html', {'category': category, 'articles': articles})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)  # Вход пользователя после регистрации
            return redirect('home')  # Перенаправление на домашнюю страницу
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на домашнюю страницу после успешного входа
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'delete_category.html', {'category': category})

