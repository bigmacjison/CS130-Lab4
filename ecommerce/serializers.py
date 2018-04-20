from rest_framework impoert serializers
from ecommerce.models import User, Cart, Product

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email_text = serializers.EmailField(max_length=50)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    shipping_address = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        #Create and return a new 'User' instance
        return User.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        #Update and return an existing 'User' instance
        instance.email_text = validated_data.get('email_text', instance.email_text)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.shipping_address = validated_data.get('shipping_address', instance.shipping_address)
        instance.save()
        return instance
        
class CartSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    cart_code = serializers.CharField(max_length=10)
    total_price = serializers.FloatField(default=0)
    cart_paid = serializers.BooleanField(default=False)
    cart_created = serializers.DateTimeField()
    cart_updated = serializers.DateTimeField()
    
    def create(self, validated_data):
        #Create and return a new 'Cart' instance
        return Cart.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        #Update and return an existing 'Cart' instance
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.cart_code = validated_data.get('cart_code', instance.cart_code)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.cart_paid = validated_data.get('cart_paid', instance.cart_paid)
        instance.cart_created = validated_data.get('cart_created', instance.cart_created)
        instance.cart_updated = validated_data.get('cart_updated', instance.cart_updated)
        instance.save()
        return instance
        
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cart_id = serializers.IntegerField(read_only=True)
    product_price = serializers.CharField(max_length=200)
    product_name = serializers.CharField(max_length=200)
    product_description = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        #Create and return a new 'Product' instance
        return Product.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        #Update and return an existing "Product' instance
        instance.cart_id = validated_data.get('cart_id', instance.cart_id)
        instance.product_price = validated_data.get('product_price', instance.product_price)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.product_description = validated_data.get('product_description', instance.product_description)
        instance.save()
        return instance