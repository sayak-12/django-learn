from django.http import HttpResponse
def home(req):
    return HttpResponse("This is the home page")
def about(req):
    return HttpResponse("this is the about page")
