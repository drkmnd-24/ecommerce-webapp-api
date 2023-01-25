from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages

from account.models import *
from basket.basket import *
from .models import *


@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, 'checkout/delivery_choices.html', {'deliveryoptions': deliveryoptions})


# this is test
@login_required
def basket_update_delivery(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        delivery_option = int(request.POST.get('deliveryoption'))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price})
        return response


@login_required
def delivery_address(request):
    session = request.session
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    addresses = Address.objects.filter(customer=request.user).order_by("-default")

    return render(request, "checkout/delivery_address.html")
