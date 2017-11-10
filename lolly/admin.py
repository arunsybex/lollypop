from django.contrib import admin
from lolly.models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
     list_display = ('id','phone_number',)
     search_fields = ('id','phone_number',)
admin.site.register(Customer,CustomerAdmin)

class DiscountAdmin(admin.ModelAdmin):
     list_display = ('id','discount_name','discount_percent',)
     search_fields = ('id','discount_name',)
admin.site.register(Discount,DiscountAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_code','item_size','item_count','price','discount',)
    list_filter = ('item_category','item_gender','item_size',)
    search_fields = ('item_code','item_name')
admin.site.register(Item,ItemAdmin)

class BillingAdmin(admin.ModelAdmin):
    list_display = ('item','id','customer','billed_by','bill_created','price',)
    list_filter = ('bill_created',)
    search_fields = ('customer','item',)
admin.site.register(Billing,BillingAdmin)
