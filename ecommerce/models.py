from django.db import models

# Create your models here.

class User(models.Model):
    email_text = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=200)
    def __str__(self):
	    return self.first_name
    def email(self):
	    return self.email_text
    def lastname(self):
	    return self.last_name
    def address(self):
	    return self.shipping_address


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_code = models.CharField(max_length=10)
    total_price = models.FloatField(default=0)
    cart_paid = models.BooleanField(default=False)
    cart_created = models.DateTimeField('date created')
    cart_updated = models.DateTimeField('date updated')
    def __str__(self):
	    return self.cart_code
    def totalprice(self):
	    return self.total_price
    def is_cartPaid(self):
	    return self.cart_paid
    def when_created(self):
	    return self.cart_created
    def when_updated(self):
	    return self.cart_updated
	
class Product(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_price = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    def __str__(self):
	    return self.product_name
    def price(self):
	    return self.product_price
    def description(self):
	    return self.product_description