from django.shortcuts import render, redirect
from .models import *
from django.db import IntegrityError
from company.models import Company
from offers.models import Offer 
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login

def createcompany(request):
    context = {}
    string = []
    if request.method == "POST" and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        name = request.POST.get("name")
        people = request.POST.get("people")
        location = request.POST.get("location")
        description = request.POST.get("description")
        count_workers = request.POST.get("count_workers")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # if len(phone) == 10:
        if people != 'number':

            try:
                user = User.objects.create_user(password=password, 
                                                username=email)
                company = Company.objects.create(name=name,
                    count_workers=count_workers, location=location, phone=phone,
            email=email, description=description, user=user, photo = file_url)
                login(request, user)
            except IntegrityError:
                print('hiii')
                context['error'] = 'Invalid'
                
            
        else:
            context['error'] = 'Тільки цифри'               
        # else:
        #     context['error'] = 'Не правильний'
        return redirect('main')
    return render(request, 'main/create_company.html', context=context)
# Create your views here.
def usercompany(request):
    if request.user.is_authenticated:
        try:
            company = Company.objects.get(user = request.user)
            offers = Offer.objects.filter(company = company)
            context = {'offers': offers}
        except:
            return redirect('main')
        return render(request, 'main/reviewavoidance2.html', context=context)
    else:
        return redirect('main', context)

def maincompany(request, id):
    company = Company.objects.get(pk=id)
    offers = Offer.objects.filter(company=company)
    context = {'company': company, 'offers': offers}
    return render(request, 'main/maincompany.html', context)