from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse ("Welcome to about us page")
def contactus(request):
    return HttpResponse ("this is contact us page")
def homepage(request):
    return render (request,"index.html")