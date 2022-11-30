import stripe
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from item.models import Item, Order
from stripe_api.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY


stripe.api_key = STRIPE_SECRET_KEY


def get_session_id(items):
    domain = "http://127.0.0.1:8000"
    list_of_items = []
    for item in items:
        list_of_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        })
    session = stripe.checkout.Session.create(
        line_items=list_of_items,
        mode='payment',
        success_url=domain + '/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=domain + '/cancel/',
    )
    return JsonResponse({'id': session.id})


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(
        request, 'item.html', {
            'item': item,
            'price': '{0:.2f}'.format(item.price / 100),
            'stripe_public_key': STRIPE_PUBLIC_KEY,
        }
    )


def buy(_, id):
    return get_session_id([get_object_or_404(Item, id=id)])


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    total_price = Item.objects.filter(orders=order).aggregate(Sum('price'))
    return render(
        request, 'order.html', {
            'order': order,
            'total_price': '{0:.2f}'.format(total_price['price__sum'] / 100),
            'stripe_public_key': STRIPE_PUBLIC_KEY,
        }
    )


def buy_order(_, id):
    return get_session_id(Item.objects.filter(orders=id))


def cancel(request):
    return render(request, 'cancel.html')


def success(request):
    return render(request, 'success.html')
