from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.forms import Newuserform
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'variable': 'this is sent'}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


@login_required(login_url='/login')
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

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Incorrect username or password. Please try again.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been logged out.')
        # CustomLogoutView inherits the logout behavior of the LogoutView class, and then adds an additional step to display a success message.
        return super().dispatch(request, *args, **kwargs)


def register(request):
    if request.method == 'POST':
        form = Newuserform(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, 'Registration Successful. Login to your account.')
            return redirect('login')
    else:
        form = Newuserform()
    return render(request, 'register.html', {'form': form})
