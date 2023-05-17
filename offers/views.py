from django.shortcuts import render
from .models import *

def the_main(request):
    a = Offer.objects.all()
    

    return render(request, 'main/main.html', {'a': a} )


def offer_page(request, id):
    offer = Offer.objects.get(pk = id)
    context = {'offer': offer}
    return render(request, 'main/offerspage.html', context=context)


def register(request):
    
    return render(request, 'main/reg.html')

def auth(request):
    
    return render(request, 'main/auth.html')
# Create your views here.
