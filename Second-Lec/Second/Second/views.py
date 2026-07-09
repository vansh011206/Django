from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello World This is Home")
    return render(request,'website/index.html')
    
def About(request):
    # return HttpResponse("Hello World This is About")
    return render(request,'website/about.html')
    
def Contact(request):
    # return HttpResponse("Hello World This is Contact")
    return render(request,'website/contact.html')
    