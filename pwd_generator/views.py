from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #Option 1: Return a single line response from here itself 
    #return HttpResponse('Hello there friend from <h1>def home:</h1> in views.py')

    #Option 2a: Return a static html page
    #return render(request, 'pwd_generator/home.html')

    #Option 2b: Return an html page with dynamic content
    #Passing it a dictionary with key/values
    #Reference to {{ key }} in the page will replace with the corresponding
    #value.
    return render(request, 'pwd_generator/home.html', {'password':'MySecret123'})

# Send a static form to user to provide criteria
# for creating a custom password
def form(request):
    return render(request, 'pwd_generator/form1.html')

#User submitted form with his criteria to create
# a password
def password(request):

    super_set_list = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    length = int(request.GET.get('length', 12))

    uppercase = "off"
    if request.GET.get('uppercase'):
        #uppercase = "on"
        super_set_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    for x in range(length):
        thepassword += random.choice(super_set_list)
    
    return render(request, "pwd_generator/password.html",
                  {'password':thepassword})

#Variation of form1 to show some html styling
def styling(request):
   return render(request, 'pwd_generator/styling.html') 