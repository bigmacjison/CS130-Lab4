from django.http import HttpResponse
from .models import User, Cart, Product
from django.utils import timezone
from ecommerce.serializers import UserSerializer, CartSerializer, ProductSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

class UserList(APIView):
    #List all users, or create a new user
    def get(self, request, format=None):
        users = User.object.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CartList(APIView):
   #List all carts, or create a new user
    def get(self, request, format=None):
        carts = Cart.object.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductList(APIView):
    #List all products, or create a new user
    def get(self, request, format=None):
        products = Product.object.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    #Retrieve, update or delete a user instance
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartDetail(APIView):
    #Retrieve, update or delete a cart instance
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        cart = self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetail(APIView):
    #Retrieve, update or delete a product instance
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
def index(request):
	return HttpResponse("Hello, world. You're at the e-commerce index.")

def getAllUser(request):
    all_user = User.objects.all()
    output = ', '.join([u.first_name for u in all_user])
    return HttpResponse(output)

def getUser(request, user_id):
    current_user = User.objects.get(id=user_id)
    #output = u.first_name for u in current_user
    output = current_user.first_name
    return HttpResponse(output)

#Update user first name
def updateUser(request, user_id, new_fn):
    update_user = User.objects.get(id=user_id)
    old_fn = update_user.first_name
    output = "First name of '{0}' has been changed to ".format(old_fn)
    update_user.first_name = new_fn
    update_user.save()
    newcur_fn = update_user.first_name
    output = output + "'{0}'.".format(newcur_fn)
    #output = "First name of '{0}' has been changed to '{1}'.".format(old_fn, newcur_fn)
    return HttpResponse(output)

def addUser(request, email, fn, ln, sa):
    new_user = User(email_text=email, first_name = fn, last_name = ln, shipping_address = sa)
    new_user.save()
    output = "New user has been recorded. Email: {0} Name: {1} {2} Shipping Address: {3}" \
        .format(new_user.email_text, new_user.first_name, new_user.last_name, new_user.shipping_address)
    return HttpResponse(output)
    
def getAllCart(request, userid):
    all_cart = Cart.objects.filter(user_id=userid)
    output = ', '.join([c.cart_code for c in all_cart])
    return HttpResponse(output)
    
def getCart(request, userid, cartcode):
    cart = Cart.objects.filter(user_id=userid)
    curcart = cart.get(cart_code=cartcode)
    output = curcart.cart_code
    return HttpResponse(output)
    
#Update care paid status
def updateCart(request, userid, cartcode, cartpaid):
    cart = Cart.objects.filter(user_id=userid)
    curcart = cart.get(cart_code=cartcode)
    curcart.cart_paid = cartpaid
    curcart.save()
    return HttpResponse("Update success.")
    
def addCart(request, userid, cartcode, totalprice, cartpaid):
    new_cart = Cart(user_id=userid, cart_code=cartcode, total_price=totalprice, cart_paid=cartpaid, cart_created=timezone.now(), cart_updated=timezone.now())
    new_cart.save()
    output = "New cart created with cart code {0} for user {1} and total price of {2}".format(new_cart.cart_code, new_cart.user_id, new_cart.total_price)
    return HttpResponse(output)
    
def getAllProducts(request, cartid):
    all_products = Product.objects.filter(cart_id=cartid)
    output = ', '.join([p.product_name for p in all_products])
    return HttpResponse(output)
    
#Get product given the cart id and product id
def getProduct(request, cartid, productid):
    product = Product.objects.filter(cart_id=cartid)
    curproduct = product.get(id=productid)
    output = curproduct.product_name
    return HttpResponse(output)
    
#Update product price
def updateProduct(request, cartid, productid, productprice):
    product = Product.objects.filter(cart_id=cartid)
    curproduct = product.get(id=productid)
    curproduct.product_price = productprice
    curproduct.save()
    return HttpResponse("Update success.")
    
def addProduct(request, cartid, productname, productprice, productdesc):
    new_product = Product(cart_id=cartid, product_price=productprice, product_name=productname, product_description=productdesc)
    new_product.save()
    output = "New product added. Name: {0} Price: {1} Description: {2}".format(new_product.product_name, new_product.product_price, new_product.product_description)
    return HttpResponse(output)
"""