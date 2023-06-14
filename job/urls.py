"""job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminpanel.views import *
from job import settings
from django.conf.urls.static import static
from offers.views import *
from finder.views import *
from company.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',the_main, name='main'),
    path('offerpage/<int:id>/',offer_page, name='offer_page'),
    path('register/',register),
    path('auth/',auth, name='auth'),
    path('user/',user, name='user'),
    path('my_resume/', resume),
    path('my_reviews/', reviews),
    path('personaldata/', personaldata),
    path('logoutuser/', logoutuser),
    path('', redirect_to_main),
    path('avoidance/', avoidance),
    path('create_avoidance/', createavoidance),
    path('review_avoidance/',reviewavoidance),
    path('create_company/', createcompany),
    path('profileredirect/', profileredirect),
    path('usercompany/', usercompany, name='usercompany'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
