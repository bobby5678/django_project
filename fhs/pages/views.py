from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = UserRegistrationForm()
        
    context = {'form': form}
    return render(request, 'pages/register.html', context)


def bid(request,food_id,user_id):
    product = Product.objects.get(id=food_id)
    userid=User.objects.get(id=user_id)
    
    product_item = ProductItem.objects.create(
                biduser=userid,
                item=product,
                bid=request.POST['bidprice'],
                )
    product_item.save()
    return redirect('home')    


def food(request):

    food_list = Product.objects.all()
    context = {'food_list': food_list}
    return render(request, 'pages/homepage.html', context)

# def search_food(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         foods = Food.objects.filter(Food_name__contains=searched)
#         return render(request,'pages/search.html',{'searched':searched,'foods':foods})

def profile(request):
    return render(request,'pages/profile.html')

# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

# def add_cart(request, product_id):
#     try:
#         food = Product.objects.get(id=product_id)

#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(
#                     cart_id = _cart_id(request)
#             ) 
#             cart.save()
#         try:
        
#             product_item = CartItem.objects.get(item=food, cart=cart)
#             cart_item.quantity += 1
#             cart_item.save()           

#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                 item=food,
#                 bid=1,
#                 
#             )
#             cart_item.save()
#         return redirect('cart')

#     except Food.DoesNotExist:
#         food =  Diet.objects.get(id=food_id)
#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(
#                 cart_id = _cart_id(request)
#             ) 
#             cart.save()
#         try:
#             cart_item = CartItemDiet.objects.get(item=food, cart=cart)
#             cart_item.quantity += 1
#             cart_item.save()
#         except CartItemDiet.DoesNotExist:
#             cart_item = CartItemDiet.objects.create(
#                 item=food,
#                 quantity=1,
#                 cart=cart
#             )
#             cart_item.save()
#         return redirect('cart')



# def cart(request, total=0, counter=0, cart_items=None):
#     try:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#     except:
#         return render(request,'pages/empcart.html')
#     cart_items = CartItem.objects.filter(cart=cart, active=True)
#     cart_itemsD = CartItemDiet.objects.filter(cart=cart, active=True)
#     if cart_items and cart_itemsD:
#         for cart_item in cart_items:
#             total += (cart_item.item.Food_price * cart_item.quantity)
#             counter += cart_item.quantity
#         for cart_item in cart_itemsD:
#             total += (cart_item.item.Food_price * cart_item.quantity)
#             counter += cart_item.quantity
#         context = {'cart_items': cart_items,'cart_itemsD': cart_itemsD, 'total': total, 'counter': counter}
#         return render(request, 'pages/cart.html', context)
#     elif not (cart_items):
#         if not (cart_itemsD):
#             return render(request,'pages/empcart.html')
#         for cart_item in cart_itemsD:
#             total += (cart_item.item.Food_price * cart_item.quantity)
#             counter += cart_item.quantity
#         context = {'cart_items': cart_itemsD, 'total': total, 'counter': counter}
#         return render(request, 'pages/cart.html', context)
        
#     else:
#         for cart_item in cart_items:
#             total += (cart_item.item.Food_price * cart_item.quantity)
#             counter += cart_item.quantity
#         context = {'cart_items': cart_items, 'total': total, 'counter': counter}
#         return render(request, 'pages/cart.html', context)

# def cart_remove(request, product_id):
#     cart = Cart.objects.get(cart_id=_cart_id(request))
#     try:
#         product = get_object_or_404(Food, id=product_id)
#         cart_item = CartItem.objects.get(item=product, cart=cart)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#         return redirect('cart')
#     except:
#         product = get_object_or_404(Diet, id=product_id)
#         cart_item = CartItemDiet.objects.get(item=product, cart=cart)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#         return redirect('cart')        


# def cart_remove_product(request, product_id):
#     cart = Cart.objects.get(cart_id=_cart_id(request))
#     try:
#         product = get_object_or_404(Food, id=product_id)
#         cart_item = CartItem.objects.get(item=product, cart=cart)
#         cart_item.delete()
#         return redirect('cart')
#     except:
#         product = get_object_or_404(Diet, id=product_id)
#         cart_item = CartItemDiet.objects.get(item=product, cart=cart)
#         cart_item.delete()
#         return redirect('cart')       


# def diet(request):

#     diet_list = Diet.objects.all()
#     context = {'diet_list': diet_list}
#     return render(request, 'pages/diet.html', context)


        



    


