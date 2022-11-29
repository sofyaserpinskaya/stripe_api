import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from item.models import Item
from stripe_api.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY

stripe.api_key = STRIPE_SECRET_KEY


def buy(request, id):
    item = get_object_or_404(Item, id=id)
    domain = "http://127.0.0.1:8000"
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
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


def cancel(request):
    return render(request, 'cancel.html')


def success(request):
    return render(request, 'success.html')
