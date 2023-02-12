from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


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


class customloginview(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return (reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
