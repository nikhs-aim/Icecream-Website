from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


def index(request):
    context = {'variable': 'this is sent'}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":   # if someone has posted it will run
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, phone=phone,
                          query=query, date=datetime.today())
        contact.save()
        messages.success(request, 'Your query has been submitted')
    return render(request, 'contact.html')
