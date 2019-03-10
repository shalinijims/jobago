from django.shortcuts import get_object_or_404,render, redirect

def home(request):
        return render(request,'home.html')




def schedulePage(request):
        return render(request,'schedulePage.html')


def login(request):
        return render(request,'login.html')