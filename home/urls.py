
from django.contrib import admin
from django.urls import path
from home import views
from .views import CustomLogoutView, customloginview


urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('login/', customloginview.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register', views.register, name='register')

]
