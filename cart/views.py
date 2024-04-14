from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Products

# Create your views here.
@login_required
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    for cart_item in cart_items:
        cart_item.total_price = cart_item.product.price * cart_item.quantity
        
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    print(context)
    return render(request,'cart.html',context)


@login_required
def add_to_cart(request,product_id):
    if request.method=='POST':
        user = request.user
        product = get_object_or_404(Products, id=product_id)
        quantity = request.POST.get('product-quantity', 1)
        # Check if the product is already in the user's cart
        existing_cart_item = Cart.objects.filter(user=user, product=product).first()
        if existing_cart_item:
            # If the product is already in the cart, update the quantity
            existing_cart_item.quantity += int(quantity)
            existing_cart_item.save()
        else:
            # If the product is not in the cart, create a new cart item
            cart_item = Cart.objects.create(user=user, product=product, quantity=quantity)

        return redirect('/shop/cart')
    else:
        pass