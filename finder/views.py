from django.shortcuts import render
from  .models import *
from django.db import IntegrityError
from company.models import Company


def user(request):
    
    return render(request, 'main/finder.html')

def resume(request):
    
    return render(request, 'main/resumefinder.html')

def reviews(request):
    company = Company.objects.get(user = request.user)

    return render(request, 'main/myreviews.html',{'companys':company} )

def personaldata(request):

    return render(request, 'main/personaldata.html')

def avoidance(request):

    return render(request, 'main/avoidance.html')

def createavoidance(request):
    
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        location = request.POST.get("location")
        description = request.POST.get("description")
        phone = request.POST.get("phone")
        min_sellary = request.POST.get("min_sellary")
        surname = request.POST.get("surname")

        if len(phone) >= 4:
            try:
                company = Company.objects.create(name=name, location=location, phone=phone,
            description=description)
                
            except IntegrityError:
                context['error'] = 'Invalid'         
        else:
            context['error'] = 'Не правильний'

    return render(request, 'main/createavoidance.html', context=context)

def reviewavoidance(request):
    
    return render(request, 'main/reviewavoidance.html')
# Create your views here.
