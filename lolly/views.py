from django.shortcuts import render,redirect
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
import json,datetime
from lolly.models import *
from django.db.models import Max
#from django.contrib.auth import login as auth_login

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')
def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['userpass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponse('success');
        else:
            return HttpResponse('Not Matched')
    elif request.method == "GET":
        if request.user.is_authenticated():
            return HttpResponseRedirect('/dashboard')
        else:
            return render(request,'login.html');

def auth_logout(request):
    logout(request);
    return HttpResponseRedirect('/');
def dashboard(request):
    if request.user.is_authenticated():
        return render(request,"bill/bill.html")
    else:
        return redirect("/login")
@login_required
def customers(request):
    return HttpResponse("arun");

@login_required
def billAdd(request):
    if request.method == "POST":
        if Billing.objects.all().aggregate(Max('bill_id'))['bill_id__max'] is None:
            bill_id = 1;
        else:
            bill_id=Billing.objects.all().aggregate(Max('bill_id'))['bill_id__max'] + 1;
        for li in json.loads(request.POST['bill_list']):
            product_detail = Item.objects.get(item_code = li["code"])
            customer_detail = Customer.objects.filter(phone_number = li["customer"])

            if len(customer_detail) == 0:
                cus = Customer(phone_number=li["customer"])
                cus.save()
            customer_detail = Customer.objects.get(phone_number = li["customer"])
            discount_data = Discount.objects.get(id = li["discount_id"])
            now = datetime.datetime.now()
            bill = Billing(bill_id=bill_id,item = product_detail,customer=customer_detail,bill_discount=discount_data,billed_by= User.objects.get(username=request.user),quantity=li["qty"],price=li["amount"]);
            bill.save()
        return HttpResponse("kao")

def product_detail(request):
    if request.method == "POST":
        #product_detail = Item.objects.filter(item_code = json.loads(request.body)['code'])
        product_detail = Item.objects.filter(item_code = request.POST['code'])
        data = serializers.serialize('json', product_detail)
        data =  json.loads(data)
        print data
        if len(product_detail) > 0:
            discount_data = Discount.objects.filter(id = data[0]["fields"]["discount"])
            for discount in discount_data:
                data[0]["fields"]["discount_percent"] = discount.discount_percent
        else:
            data = {"error":1}
        return HttpResponse(json.dumps(data), content_type="application/json")

def customer_detail(request):
    if request.method == "POST":
        customer_detail = Customer.objects.filter(phone_number = request.POST['c_code'])
        data = serializers.serialize('json', customer_detail)
        data =  json.loads(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
