from django.shortcuts import render

def home(request):
    names = [
        "Amit",
        "Rahul",
        "Priya",
        "Neha",
        "Suresh"
    ]
    return render(request,'websites/index.html',{'pagename':names})
def about(request):
    return render(request,'websites/about.html',{'pagename':'About'})