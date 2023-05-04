from django.shortcuts import render


def user(request):
    
    return render(request, 'main/finder.html')

def resume(request):
    
    return render(request, 'main/resumefinder.html')
# Create your views here.
