from django.shortcuts import render

# Create your views here.
def oneside(request):
    return render(request,'oneside.html')

def commited(request):
    return render(request,'commited.html')

def breakup(request):
    return render(request,'breakup.html')

def singles(request):
    return render(request,'singles.html')