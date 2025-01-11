from .models import Product, Category, OrderItem, Order, Recommended, Cart, CartItem
from .serializers import HomeSerializers, CategorySerializers, RecommendedSerializers, jsonOrder, jsonOrderItem, ProductFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import request
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .filters import ProductFilter
from rest_framework import generics
from django_filters import rest_framework as filters
from django.http import HttpResponse
# from authentications.models import User


# @api_view(['Post','GET'])
# def Home_listAPI(request):
#     all_ads=Products.objects.all()
#     permission_classes = [permissions.IsAdminUser]
#     return Response(HomeSerializers(all_ads,many=True).data)


@api_view(['GET', 'Post'])
def Recommended_listAPI(request):
    all_ads = Recommended.objects.all().distinct()
    # permission_classes = [permissions.IsAdminUser]
    return Response(RecommendedSerializers(all_ads, many=True).data)


class product(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = HomeSerializers
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


# @api_view(['GET', 'Post'])
@login_required
def product_listAPI(request):
    all_ads = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=all_ads)
    all_ads = product_filter.qs

    paginator = Paginator(all_ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj,
               'product_filter': product_filter, 'all_products': all_ads}
    return render(request, 'home/product_list.html', context)
    # return Response(CategorySerializers(all_ads,many=True).data)


def product_detail(request, id):
    all_ads = Product.objects.get(product_id=id)
    context = {'product': all_ads}
    return render(request, 'home/product_detail.html', context)


@api_view(['GET', 'Post'])
def Categories_listAPI(request):
    all_ads = Category.objects.all()
    context = {'categories': all_ads}
    return render(request, 'home/category_list.html', context)


def Categories_detail(request, id):
    all_ads = Category.objects.get(category_id=id)
    catts = all_ads.category_products.all()
    context = {'category': all_ads,
               'catts': catts}
    return render(request, 'home/category_detail.html', context)


@api_view(['GET', 'Post'])
def Category_listAPI(request):
    all_ads = Category.objects.all()
    # context={'categories':all_ads}
    # return render(request,'home/category_list.html',context)
    return Response(CategorySerializers(all_ads, many=True).data)


# REST API
@api_view(['GET'])
def Category_detail(request, id):
    all_ads = Category.objects.get(category_id=id)
    return Response(CategorySerializers(all_ads).data)


class orderitem(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = jsonOrderItem


class order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = jsonOrder


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('home:cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, product_id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('home:cart')


def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, product_id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('home:cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except:
        pass
    context = {
        "cart_items": cart_items,
        "total": total,
        "quantity": quantity,
    }

    return render(request, 'home/cart.html', context)


def Order_list(request):
    all_list = OrderItem.objects.all()
    context = {'cart': all_list}
    return render(request, 'l', context)
