from django.shortcuts import render,redirect
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
import json
from lolly.models import *
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
    return HttpResponse("kao")

def product_detail(request):
    if request.method == "POST":
        #product_detail = Item.objects.filter(item_code = json.loads(request.body)['code'])
        product_detail = Item.objects.filter(item_code = request.POST['code'])
        data = serializers.serialize('json', product_detail)
        data =  json.loads(data)
        if len(product_detail) > 0:
            discount_data = Discount.objects.filter(id = data[0]["fields"]["discount"])
            for discount in discount_data:
                data[0]["fields"]["discount"] = discount.discount_percent
        else:
            data = {"error":1}
        return HttpResponse(json.dumps(data), content_type="application/json")

def customer_detail(request):
    if request.method == "POST":
        customer_detail = Customer.objects.filter(phone_number = request.POST['c_code'])
        data = serializers.serialize('json', customer_detail)
        data =  json.loads(data)
        return HttpResponse(json.dumps(data), content_type="application/json")
