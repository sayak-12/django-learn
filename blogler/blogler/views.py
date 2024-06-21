from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    # return HttpResponse("This is the home page")
    return render(req, 'home.html')
def about(req):
    # return HttpResponse("this is the about page")
    return render(req, 'about.html')
