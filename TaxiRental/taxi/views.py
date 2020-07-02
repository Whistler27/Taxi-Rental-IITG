from django.http import HttpResponse
from django.shortcuts import render
from . models import Contact

def index(request):
    return render(request,'taxi/index.html')

def info(request):
    return render(request,'taxi/info.html')

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get("Email")
        message = request.POST.get("Message")
        contact = Contact(name = name,email = email,message = message)
        contact.save()
        thank = True
    return render(request, 'taxi/contact.html', {'thank': thank})

    

