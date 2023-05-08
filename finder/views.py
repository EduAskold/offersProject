from django.shortcuts import render


def user(request):
    
    return render(request, 'main/finder.html')

def resume(request):
    
    return render(request, 'main/resumefinder.html')

def reviews(request):

    return render(request, 'main/myreviews.html')

def personaldata(request):

    return render(request, 'main/personaldata.html')
# Create your views here.
