from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product,Variation
from .models import Cart, CartItems

from django.http import HttpResponse
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart =request.session.create()

    return cart

def add_cart(request, product_id):
    product= Product.objects.get(id=product_id)
    product_variation=[]
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.objects.get(product = product ,variation_category__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)
            except :
                pass
                
    product = Product.objects.get(id = product_id)#get the product
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))# get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    is_cart_item_exists = CartItems.objects.filter(product=product,cart=cart).exists()

    if is_cart_item_exists:
        cart_item = CartItems.objects.filter(product = product,cart=cart)
        ex_var_list = []
        id=[]
        for item in cart_item:
            existing_variation = list(item.variations.all())
            ex_var_list.append(existing_variation)
            id.append(item.id)
        print(ex_var_list)

        if product_variation in ex_var_list:
            index   = ex_var_list.index(product_variation)
            item_id = id[index]
            item    = CartItems.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()
        else:
            item = CartItems.objects.create(product = product,quantity=1,cart=cart)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()
    else:
        cart_item = CartItems.objects.create(product = product, quantity=1, cart=cart,)
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()
    return redirect('cart')

def remove_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product =get_object_or_404(Product, id = product_id)
    try:
        cart_item =CartItems.objects.get(product = product, cart=cart,id= cart_item_id)
        if cart_item.quantity > 1:
             cart_item.quantity -= 1
             cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request, product_id,cart_item_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product =get_object_or_404(Product, id = product_id)
    cart_item =CartItems.objects.get(product = product, cart=cart,id =cart_item_id)

    cart_item.delete()
    return redirect('cart')


def cart(request, total = 0, quantity=0, cart_items = None ):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItems.objects.filter(cart = cart, is_active = True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity +=cart_item.quantity
        tax = (3*total)/100
        grand_total = total + tax
    except ObjectNotExist:
            pass

    context = {
            'total': total,
            'quantity' : quantity,
            'cart_items' : cart_items,
            'tax': tax,
            'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)
