from django.contrib import admin
from django.db.models import Sum
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')
    list_filter = ('orders',)
    search_fields = ('name__startswith',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'view_items_link', 'total_cost')

    def total_cost(self, obj):
        result = Item.objects.filter(orders=obj).aggregate(Sum('price'))
        return result['price__sum']

    def view_items_link(self, obj):
        count = obj.items.count()
        url = (
            reverse("admin:item_item_changelist") + "?"
            + urlencode({"orders__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Items</a>', url, count)

    view_items_link.short_description = "Items"
