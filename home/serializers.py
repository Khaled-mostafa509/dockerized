from rest_framework import serializers
from .models import Product , Order , OrderItem ,Recommended,Category 
from django_filters import rest_framework as filters

        
class HomeSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['product_id','Name','description','category','price','Production_country','image','user']

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['Name','category', 'Production_country']

class HomeRecommendSerializers(serializers.ModelSerializer):
    category=serializers.CharField()
    user= serializers.CharField()
    class Meta:
        model = Product
        fields = ['product_id','Name','description','category','price','Production_country','image','user']
    
class CategorySerializers(serializers.ModelSerializer):
    category_products =  HomeSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_id','Name','category_products']
        
class RecommendedSerializers(serializers.ModelSerializer):
    product_name= HomeRecommendSerializers(read_only=True,)
    recomended_devices =  HomeRecommendSerializers(many=True, read_only=True,)
    class Meta:
        model = Recommended
        fields = ['product_name','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"
        
class  jsonOrder(serializers.ModelSerializer):
    # items= serializers.CharField(source=f"{OrderItem.quantity} of {OrderItem.item}")
    class Meta:
        model = Order
        fields = "__all__"      
        
