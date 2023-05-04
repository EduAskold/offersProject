from django.shortcuts import render

def the_main(request):
    
    return render(request, 'main/main.html')


def offer_page(request):
    
    return render(request, 'main/offerspage.html')

def register(request):
    
    return render(request, 'main/reg.html')

def auth(request):
    
    return render(request, 'main/auth.html')
# Create your views here.
