from django.urls import path

from .views import (
    ProfileView,DashboardView,HomeView
   
)
from . import views


app_name = 'applicant'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('sign-up/', views.register, name='sign_up'),
    path('log-in/', views.login, name='log_in'),
    path('schedule/', views.schedule, name='schedule'),
    path('log-out/', views.logout, name='log_out'),
    path('dashboard',DashboardView.as_view(), name='dashboard'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('basicDetail',views.saveBasic,name='basic'),
    path('educationDetail',views.saveEducation,name='education'),



    #ajax function
    path('getstate',views.getstate,name='getstate'),
    path('getcourse',views.getcourse,name='getcourse'),

 
]
