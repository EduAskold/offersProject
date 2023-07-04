from django.shortcuts import render, redirect
from  .models import *
from django.db import IntegrityError
from company.models import Company
from offers.models import Offer, Category


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
    categories = Category.objects.all() 
    # Допуск на сторінку тільки якщо користувач авторізувався
    if request.user.is_authenticated:
        # Пробуємо перевірити чи прив'язана до цього користувача компанія
        try:
            company = Company.objects.get(user = request.user) 
        except:
            # Якщо компанія не прив'зана то користувач не може створити вакансію і ми його повертаємо на головну сторінку
            return redirect('main')
        context = {}
        if request.method == "POST":
            name = request.POST.get("name")
            location = request.POST.get("location")
            description = request.POST.get("description")
            requirements = request.POST.get("requirements")
            offers = request.POST.get("offers")
            min_selary = request.POST.get("min_sellary")
            max_selary = request.POST.get("max_sellary")
            category = request.POST.get("category")


            try:
                category = Category.objects.get(pk=category)
                offer = Offer.objects.create(name = name,
                                            location=location,
                                            description=description,
                                            requirements=requirements,
                                            offers=offers,
                                            min_selary=min_selary,
                                            max_selary=max_selary,
                                            is_remote = True,
                                            category=category,
                                            company=company
                                            )
            except IntegrityError:
                context['error'] = 'Invalid'         
        context['categories'] = categories
        return render(request, 'main/createavoidance.html', context=context)
    else:
        return redirect('main')
def reviewavoidance(request):
    user = request.user
    company = Company.objects.get(user = user)
    
    return render(request, 'main/reviewavoidance.html', {'companys': company})
# Create your views here.
