from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getalluser', views.getAllUser, name='getAll'),
    path('getuser/<int:user_id>', views.getUser, name='getOne'),
    path('updateuser/<int:user_id>/<str:new_fn>', views.updateUser, name='updateUser'),
    path('adduser/<str:email>+<str:fn>+<str:ln>+<str:sa>', views.addUser, name='addUser'),
    path('getallcart/<int:userid>', views.getAllCart, name='getAllCart'),
    path('getcart/<int:userid>/<str:cartcode>', views.getCart, name='getCart'),
    path('updatecart/<int:userid>/<str:cartcode>/<str:cartpaid>', views.updateCart, name='updateCart'),
    path('addcart/<int:userid>/<str:cartcode>+<int:totalprice>+<str:cartpaid>', views.addCart, name='addCart'),
    path('getallproducts/<int:cartid>', views.getAllProducts, name='getAllProducts'),
    path('getproduct/<int:cartid>/<int:productid>', views.getProduct, name='getProduct'),
    path('updateproduct/<int:cartid>/<int:productid>/<int:productprice>', views.updateProduct, name='updateProduct'),
    path('addproduct/<int:cartid>/<str:productname>+<int:productprice>+<str:productdesc>', views.addProduct, name='addProduct'),
]