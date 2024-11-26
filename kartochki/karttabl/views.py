from django.shortcuts import render

# Create your views here.
from .models import Clothes, Electronics, Car, Jewelry, HomeAppliance

def product_list(request):
    clothes = Clothes.objects.all()
    electronics = Electronics.objects.all()
    cars = Car.objects.all()
    jewelry = Jewelry.objects.all()
    home_appliances = HomeAppliance.objects.all()

    context = {
        'clothes': clothes,
        'electronics': electronics,
        'cars': cars,
        'jewelry': jewelry,
        'home_appliances': home_appliances,
    }
    
    return render(request, 'karttabl/product_list.html', context)