from django.shortcuts import render
from django.http import HttpResponse
from .models import Robots,Wasteitems

def home(request):
    return render( request, 'main_page/home.html')

def dashboard(request):

    context = {
        'robots' : Robots.objects.all()
    }
    return render(request, 'main_page/display_dashboard.html',context)
