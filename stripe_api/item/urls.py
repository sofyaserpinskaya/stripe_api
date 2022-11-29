from django.urls import path

from . import views


app_name = 'items'

urlpatterns = [
    path('buy/<int:id>/', views.buy, name='buy'),
    path('buy_order/<int:id>/', views.buy_order, name='buy_order'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
]
