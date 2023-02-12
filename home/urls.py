
from django.contrib import admin
from django.urls import path
from home import views
from .views import customloginview
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('login/', customloginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),



]
