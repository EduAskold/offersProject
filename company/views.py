from django.shortcuts import render
from .models import *
from django.db import IntegrityError

def createcompany(request):
    context = {}
    string = []
    if request.method == "POST":
        name = request.POST.get("name")
        people = request.POST.get("people")
        location = request.POST.get("location")
        description = request.POST.get("description")
        count_workers = request.POST.get("count_workers")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if len(phone) >= 4:
            if people != 'number':

                try:
                    user = User.objects.create_user(password=password, 
                                                    username=email)
                    company = Company.objects.create(name=name,
                        count_workers=count_workers, location=location, phone=phone,
                email=email, description=description, user=user)
                    
                except IntegrityError:
                    context['error'] = 'Invalid'
                 
               
            else:
                context['error'] = 'Тільки цифри'               
        else:
            context['error'] = 'Не правильний'
    return render(request, 'main/create_company.html', context=context)
# Create your views here.
