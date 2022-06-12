from django.contrib import admin

from .models import Profile,Product,OrderIteam,ShipppingInformation,Order


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   list_display:['id','Name','location']

@admin.register(Product)   
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','Name','Price']    
@admin.register(OrderIteam)
class OrderIteamAdmin(admin.ModelAdmin):
    list_display=['id','Quantity']
@admin.register(ShipppingInformation)
class OrderIteamAdmin(admin.ModelAdmin):
    list_display=['id','Name','City']
@admin.register(Order)
class OrderIteamAdmin(admin.ModelAdmin):
    list_display=['id','customer']

