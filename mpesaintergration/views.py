from django.shortcuts import render
from django_daraja.mpesa import utils
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import  MpesaClient
from decouple import config
from datetime import datetime


cl=MpesaClient()
stk_push_callback_url='https://api.darajajambili.com/express-payment'
b2c_callback_url='https://api.darajajambili.com/bz2.result'

def auth_success(request):
    r=cl.auth_token()
    return JsonResponse(r, safe=False)



def index(request):
    if request.method=="POST":
        phone_number=request.POST.get('phone')
        amount=request.POST.get('amount')
        amount=int(amount)
        account_refrence='FAVOUR'
        transaction_refrence='STK pusg despcription'
        callback_url=stk_push_callback_url
        r = cl.stk_push(phone_number,amount,account_refrence,transaction_refrence,callback_url)
        return JsonResponse(r.response_description,safe=False)
    return render(request,'index.html')
