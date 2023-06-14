from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError

def the_main(request):
    a = Offer.objects.all()
    

    return render(request, 'main/main.html', {'offers': a} )


def offer_page(request, id):
    offer = Offer.objects.get(pk = id)
    context = {'offer': offer}
    return render(request, 'main/offerspage.html', context=context)


def register(request):
    context = {}
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        location = request.POST.get("location")
        password = request.POST.get("password")
        repidpassword = request.POST.get("repidpassword")

        if len(password) >= 4:
            if password == repidpassword:
                if password != email and firstname and lastname and location:
                    try:
                        
                        user = User.objects.create_user(password=password, first_name=firstname, last_name=lastname, username=email)
                        finder = Finder.objects.create( user = user, location = location, name = firstname, surname = lastname, email = email )
                        return redirect('auth')
                    except IntegrityError:
                        context['error'] = 'Користувач вже існує'
                 
                else:
                    context['error'] = 'Пароль не правильний'
            else:
                context['error'] = 'Invalid'               
        else:
            context['error'] = 'Пароль повинен мати більше 4 символів'
    return render(request, 'main/reg.html', context=context)


def auth(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            context['error'] = 'Не правильний логін або пароль'
    return render(request, 'main/auth.html', context=context)


def logoutuser(request):
    logout(request)
    return redirect('main')

def redirect_to_main(request):

    return redirect ('main')
# Create your views here.
def profileredirect(request):
    if request.user.is_authenticated:
        try:
            company = Company.objects.get(user = request.user) 
            return redirect('usercompany')
        except:
            # Якщо компанія не прив'зана то користувач - шукач роботи
            return redirect('user')

    else:
        return redirect('main')