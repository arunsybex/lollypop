from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User,Group

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 50,blank=True, null=True)
    mail = models.CharField(max_length = 50,blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, unique=True)
    status = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
      db_table = "customer"

    def __str__(self):
        return self.phone_number

class Discount(models.Model):
    discount_name = models.CharField(max_length=15, blank=True, unique=True)
    discount_percent = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "discount"

    def __str__(self):
        return self.discount_name

class Item(models.Model):
    item_code = models.CharField(max_length=50,unique=True)
    item_name = models.CharField(max_length=150)
    item_gender = models.CharField(max_length=50)
    item_size = models.CharField(max_length=150)
    item_category = models.CharField(max_length=150)
    item_descriptions = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.ForeignKey(Discount)
    timestamp = models.DateTimeField(default=timezone.now)
    item_count = models.IntegerField(blank=True, null=True)

    class Meta:
      db_table = "item"

    def __str__(self):
        return self.item_code

class Billing(models.Model):
    item = models.ForeignKey(Item)
    customer = models.ForeignKey(Customer)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    bill_discount = models.ForeignKey(Discount)
    billed_by = models.CharField(max_length=128,blank=True, null=True)
    bill_created = models.DateField(auto_now_add=True,blank=True, null=True)
    billed_timestamp = models.DateTimeField(default=timezone.now)


    class Meta:
        db_table = "billing"

    def __str__(self):
        return self.id
