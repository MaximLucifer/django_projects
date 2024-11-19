from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .cart import Cart

# Create your views here.
def product_list(request, category_slug=None):
    category=None
    categories= Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category, slug=category_slug)
        products=products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, slug):
    product=get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def cart_view(request):
    cart = Cart(request)  # Initialize the cart
    return render(request, 'shop/cart.html', {'cart': cart})

def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product, quantity)
    
    return redirect('cart')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('product_list')