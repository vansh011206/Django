from django.shortcuts import render

def home(response):
    return render(response,'website\index.html',{ "name" :"Vanshaj" })