from django.shortcuts import render
from .models import Clothing, Electronics, Automobile, HomeAppliance, Jewelry

# Create your views here.
def product_list(request):
    # Получаем все объекты из всех конкретных моделей
    clothing_products = Clothing.objects.all()
    electronics_products = Electronics.objects.all()
    automobile_products = Automobile.objects.all()
    home_appliance_products = HomeAppliance.objects.all()
    jewelry_products = Jewelry.objects.all()

    # Объединяем все продукты в один список (если необходимо)
    products = list(clothing_products) + list(electronics_products) + list(automobile_products) + list(home_appliance_products) + list(jewelry_products)

    return render(request, 'minishop/product_list.html', {'products': products})