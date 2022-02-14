from django.shortcuts import render
from .models import Project

def portfolio_about(request):
   return render(request, 'portfolio/about.html')
   
def portfolio(request):
   proj = Project.objects.all()
   return render(request, 'portfolio/home.html',
                 {'projects' : proj})
