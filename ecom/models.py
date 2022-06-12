from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    Name = models.OneToOneField(User,on_delete=models.CASCADE)
    Location = models.CharField(max_length=200)

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Images = models.ImageField(upload_to='Images')
    Price = models.IntegerField(null=True)
    

class OrderIteam(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.PROTECT,null=True)
    Product = models.ForeignKey(Product,on_delete=models.PROTECT)
    Quantity = models.IntegerField(default=0)
    Carted = models.BooleanField(default = False)
    Ordered = models.BooleanField(default='False')
   


    @property
    def total_price(self):
        price = self.Product.Price
        total_price = price*self.Quantity
        return total_price


    @property
    def grand_total(self):
        grand=sum( value  for value in self.total_price) 
        return grand   
        

   
class ShipppingInformation(models.Model):
    Name = models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Postal_code = models.CharField(max_length=100)
    location = models.CharField(max_length=100)



class Order(models.Model):
    customer = models.ForeignKey(Profile,on_delete=models.PROTECT)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Transaction_id = models.CharField(max_length=30,null=True)
    




