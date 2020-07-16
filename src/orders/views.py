from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart2.cart import Cart
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from .models import Order
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .paypal_setup import getClient, getRazorClient
from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypalhttp import HttpError
import json


def order_create(request):
    cart = Cart(request)

    client = getRazorClient(request)

    sample_data = {'id': 'inv_FFEtvHWlbi13K1', 'entity': 'invoice', 'receipt': None, 'invoice_number': None, 'customer_id': 'cust_FFEtvJZDoEgG4I', 'customer_details': {'id': 'cust_FFEtvJZDoEgG4I', 'name': 'Test Customer', 'email': 'test@example.com', 'contact': '+91-8879107992', 'gstin': None, 'billing_address': None, 'shipping_address': None, 'customer_name': 'Test Customer', 'customer_email': 'test@example.com', 'customer_contact': '+91-8879107992'}, 'order_id': 'order_FFEtvLG8anD4FL', 'line_items': [], 'payment_id': None, 'status': 'issued', 'expire_by': None, 'issued_at': 1594918278, 'paid_at': None, 'cancelled_at': None, 'expired_at': None, 'sms_status': 'pending', 'email_status': 'pending', 'date': 1594918278, 'terms': None, 'partial_payment': False, 'gross_amount': 1000, 'tax_amount': 0, 'taxable_amount': 0, 'amount': 1000, 'amount_paid': 0, 'amount_due': 1000, 'currency': 'INR', 'currency_symbol': '₹', 'description': 'payment link', 'notes': [], 'comment': None, 'short_url': 'https://rzp.io/i/cPNx0nm', 'view_less': True, 'billing_start': None, 'billing_end': None, 'type': 'link', 'group_taxes_discounts': False, 'user': None, 'created_at': 1594918278}

    print(json.dumps(sample_data['short_url']))

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                cart.clear()
                request.session['order_id'] = order.id

                amount = int(item['price'] * 100)

                DATA2 = {
                    "customer": {
                        "name": "Test Customer",
                        "email": "test@example.com",
                        "contact": "+91-8879107992"
                    },
                    "type": "link",
                    "amount": amount,
                    "currency": "INR",        
                    "description": "payment link"  
                }
                try: 
                    response = client.invoice.create(data=DATA2)
                    payment_link = response['short_url']
                    # print(response)
                except IOError as ioe:
                    print(ioe)
                
            
            return redirect('/orders/process-payment/')

        # return render(request, 'orders/created.html', {
        #     'order': order
        # })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {
        'form': form,
        'cart': cart,
        'payment_link': sample_data['short_url']
    })


def process_payment(request):
    order_id = request.session.get('order_id')
    print(order_id)
    order = get_object_or_404(Order, id = order_id)
    item_price = get_object_or_404(OrderItem, order=order)    
    price = item_price.price
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' %price,
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, redirect('/orders/payment_done/')),
        'cancel_return': 'http://{}{}'.format(host, redirect('/orders/payment_cancelled/'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    
    return render(request, 'orders/make_payment.html', {
        'order': order,
        'form': form
    })

@csrf_exempt
def payment_done(request):
    return render(request, 'orders/payment_done.html')

@csrf_exempt
def payment_cancel(request):
    return render(request, 'orders/payment_cancelled.html')
