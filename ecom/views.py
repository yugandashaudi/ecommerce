from django.shortcuts import render,redirect
from .models import Product,OrderIteam,Profile
import json 
from django.http import JsonResponse
from .forms import shippingdetails
from django.http import HttpResponse
import requests as req
import xml.etree.ElementTree as ET
import datetime
from .models import Order 


def home(request):
    if request.method =="POST":
        data =json.loads(request.body)
      
        id = data['id']
        action = data['action']
        print(action)
        active_user = Profile.objects.get(Name=request.user)
    
        product=Product.objects.get(id=id,)
        orderiteam,created = OrderIteam.objects.get_or_create(Product=product,user=active_user)
        if action == 'remove':
            orderiteam.Quantity=(orderiteam.Quantity-1)
           
           
            
        elif action =='add':   
            orderiteam.Quantity=(orderiteam.Quantity+1)
            orderiteam.Carted=True

        orderiteam.save()     

        if  orderiteam.Quantity<=0:
            orderiteam.delete()
           


       

    


    

       

        return JsonResponse('iteam was added',safe=False)

    product =Product.objects.all()
    active_user = Profile.objects.get(Name=request.user)
    orderiteam=OrderIteam.objects.filter(user= active_user)
    total =0
    for orr in orderiteam:
       
        total += orr.Quantity
    
    content ={'product':product,'value':total}
    return render(request,'home.html',content)


def checkout(request):
    if request.method =="POST":
        data =json.loads(request.body)
      
        id = data['id']
        action = data['action']
        print(action)
        orderiteam = OrderIteam.objects.get(id = id)
        if action == 'remove':
            orderiteam.Quantity=(orderiteam.Quantity-1)
           
           
            
        elif action =='add':   
            orderiteam.Quantity=(orderiteam.Quantity+1)
            orderiteam.Carted=True

        orderiteam.save()     

        if  orderiteam.Quantity<=0:
            orderiteam.delete()

        return JsonResponse('iteam was added in checkout',safe=False)
    
           
    active_user = Profile.objects.get(Name=request.user)
    orderiteam = OrderIteam.objects.filter(Carted=True,user=active_user)
   

   
    total =0
    grand_total=0
    for orr in orderiteam:
        grand_total += orr.total_price
       
        total += orr.Quantity
    

    context={'order':orderiteam,'value':total,'grand_total':grand_total}

    return render(request,'checkout.html',context)



def shipping(request):
    form = shippingdetails()
    active_user = Profile.objects.get(Name=request.user) 
    orderiteam = OrderIteam.objects.filter(Carted=True,user=active_user)
   
    total =0
    grand_total=0
    
    
    for orr in orderiteam:
        grand_total += orr.total_price
       
        total += orr.Quantity
      
    if request.method == "POST":
        form = shippingdetails(request.POST)
        if form.is_valid():
            form.save()

            return redirect('payment')


    context={'form':form,'value':total,'order':orderiteam,'grand_total':grand_total}        

    return render(request,'shipping.html',context)        



def payment(request):
    active_user = Profile.objects.get(Name=request.user) 
    orderiteam = OrderIteam.objects.filter(Carted=True,user=active_user)
    order,created = Order.objects.get_or_create(customer = active_user)
    order.Transaction_id=datetime.datetime.now().timestamp()
    print(order.Transaction_id)
   
    total =0
    grand_total=0
    
    
    for orr in orderiteam:
        grand_total += orr.total_price
        
       
        total += orr.Quantity
    context={'order':orderiteam,'grand_total':grand_total,'realorder':order.Transaction_id}     
    
    return render(request,'payment.html',context)   

def verify(request):
    if request.method=="GET":
        oid = request.GET.get('oid')
        amt = request.GET.get('amt')
        refId = request.GET.get('refId')

        url ="https://uat.esewa.com.np/epay/transrec"
        d = {
        'amt': amt,
        'scd': 'EPAYTEST',
        'rid':refId,
        'pid':oid,
        }
        resp = req.post(url, d)
        root =ET.fromstring(resp.content)
        status=root[0].text.strip()
        print(status)
        if status == "Success":
            print(status)
            return redirect('home')

        else:
            return redirect('payment')    
            

        
def failed(request):
    return HttpResponse('failed')    