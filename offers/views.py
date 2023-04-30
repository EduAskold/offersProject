from django.shortcuts import render

def the_main(request):
    
    return render(request, 'main/offers.html')


def user_page(request):
    
    return render(request, 'main/offers2.html')
# Create your views here.
