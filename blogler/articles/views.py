from django.shortcuts import render

def articles_list(req):
    return render(req, 'articles/list.html')
# Create your views here.
