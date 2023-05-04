from django.shortcuts import render

def the_main(request):
    
    return render(request, 'main/offers.html')


def user_page(request):
    
    return render(request, 'main/offers2.html')

def register(request):
    
    return render(request, 'main/offers3.html')

def open(request):
    
    return render(request, 'main/offers4.html')
# Create your views here.
