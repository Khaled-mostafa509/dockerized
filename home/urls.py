from django.urls import path, include


from . import views
from rest_framework import routers

app_name = 'home'
rr = routers.DefaultRouter()
rr.register('', views.orderitem)

rrr = routers.DefaultRouter()
rrr.register('', views.order)


r = routers.DefaultRouter()
r.register('', views.product)

urlpatterns = [
    path('ca/', views.cart, name='cart'),
    path('Category/', views.Category_listAPI, name='category'),
    path('Category/<int:id>', views.Category_detail, name='category_detail'),

    path('Category/list/', views.Categories_listAPI, name='category'),
    path('Categories/<int:id>', views.Categories_detail, name='category_detail'),

    path('', views.product_listAPI, name='product_list'),
    path('product/<int:id>', views.product_detail, name='product_detail'),

    path('cart/', views.Order_list, name='shopping_cart'),
    path('order/', include(rrr.urls)),
    path('itemorder/', include(rr.urls)),
    path('Recommended/', views.Recommended_listAPI, name='Recommended'),
    path('productAPI/', include(r.urls)),
    path('addcart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('removecart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('removecart_item/<int:product_id>/',
         views.remove_cart_item, name='remove_cart_item'),



]
