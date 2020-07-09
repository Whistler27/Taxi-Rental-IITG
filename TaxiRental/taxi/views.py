from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . models import Contact,Orders,OrderUpdate
from django.urls import reverse
from taxi.helper import get_user
from taxi.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

def index(request):
    return render(request,'taxi/index.html')

def dashboard(request):
    return render(request,'taxi/dashboard.html')

def checkout(request):
    thank = False
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        destination = request.POST.get('destination', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, email=email, destination=destination,
                        phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

                'MID': 'WorldP64425807474247',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'taxi/paytm.html', {'param_dict': param_dict})

    return render(request, 'taxi/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'taxi/paymentstatus.html', {'response': response_dict})

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get("Email")
        message = request.POST.get("Message")
        contact = Contact(name = name,email = email,message = message)
        contact.save()
        thank = True
    return render(request, 'taxi/contact.html', {'thank': thank})

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)

  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect(reverse('taxi/'))