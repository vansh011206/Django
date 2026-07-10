from django.shortcuts import render

# Create your views here.
def firstapp(request):
    return render(request,'firstapp/firstapp.html')
def secondhtml(request):
    return render(request,'firstapp/second.html')