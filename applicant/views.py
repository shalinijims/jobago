from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.tokens import default_token_generator
from django.core import serializers
from django.contrib.auth.hashers import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView,TemplateView
from django.conf import settings
from django.http import JsonResponse

from .utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)

from .models import *
from applicant.models import *
from django.shortcuts import get_object_or_404, render

from .forms import (
     SignUpForm,LoginForm
)
from django.core import serializers
from .models import *

def schedule(request):
    return render(request,'schedule.html')

class HomeView(TemplateView):
    template_name = 'home.html'

def getstate(request):
    if request.method=='GET':
        country=request.GET.get('countryId')
        allstate=State.objects.filter(country_id=country)
        try:
            if allstate:
                states = serializers.serialize('json', allstate)
                return JsonResponse(states,safe=False,status=200)
            else:
                return JsonResponse({"code":500,"data":None,"msg":"data not found"})
        except Exception as e:
            return JsonResponse({"code": 500, "data": None, "msg": "??????"})

def getcourse(request):
    if request.method=='GET':
        qualify_id=request.GET.get('qualify_id')
        allcourse=Course.objects.filter(qualify_id=qualify_id)
        try:
            if allcourse:
                course = serializers.serialize('json', allcourse)
                return JsonResponse(course,safe=False,status=200)
            else:
                return JsonResponse({"code":500,"data":None,"msg":"data not found"})
        except Exception as e:
            return JsonResponse({"code": 500, "data": None, "msg": "??????"})


def register(request):
    if request.method=='POST':
        print(request.POST)
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
             form.save()
             messages.success(request, _('You are successfully signed up!Please login now'))
             return redirect('applicant:log_in')

    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})



def login(request):
    if request.method=='POST':
        print(request.POST)
        form=LoginForm(request.POST)
        print(form.errors)
        email = request.POST.get('email')
        password = request.POST.get('password')
        if form.is_valid():
            user = Applicant.objects.get(email__iexact=email)
            print(password)
            print(user.password)
            check=check_password(password, user.password)
            if check:
                request.session['applicant_id'] = user.id
                request.session['email'] = user.email
                request.session['mobile'] = user.mobile
                request.session['is_complete']=user.profile_complete
                print(user.profile_complete)
                if(user.profile_complete):
                    return redirect('applicant:dashboard')
                else:
                    return redirect('applicant:profile')
            else:
                messages.error(request, _('Invalid password'))
                return redirect('applicant:log_in')
    else:
        form=LoginForm()
    return render(request,'log_in.html',{'form':form})



def logout(request):
    request.session.flush()
    return render(request,'log_out.html')


def saveBasic(request):
    if request.method=='POST':
        print(request.POST)
        firstname=request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        marital_status=request.POST.get('marital_status')
        dob=request.POST.get('dob')
        language=request.POST.get('language')
        country=request.POST.get('country')
        state=request.POST.get('state')
        user=Personal_detail.objects.get(applicant_id__iexact=request.session['applicant_id'])
        if user:
            user.applicant_id=request.session['applicant_id']
            user.first_name=firstname
            user.last_name=lastname
            user.gender=gender
            user.date_of_birth=dob
            user.martial_status=marital_status
            user.language_id=language
            user.country_id=country
            user.state_id=state
            user.save()
            return JsonResponse({"code": 200, "data": None, "msg": "personal detail updated"})

        else:
            user = Personal_detail.objects.create(applicant_id=request.session['applicant_id'],
                                              first_name=firstname,
                                              last_name=lastname,
                                              gender=gender,
                                              date_of_birth=dob,
                                              martial_status=marital_status,
                                              language_id=language,
                                              country_id=country,
                                              state_id=state)
            user.save()
            return JsonResponse({"code": 200, "data": None, "msg": "personal detail created"})

def saveEducation(request):
    if request.method == 'POST':
        print(request.POST)
        Qualification = request.POST.get('qualification')
        course = request.POST.get('course')
        institute = request.POST.get('institute')
        specialization = request.POST.get('specialization')
        coursetype = request.POST.get('coursetype')
        passyear = request.POST.get('passyear')
        user = Education_detail.objects.get(applicant_id__iexact=request.session['applicant_id'])
        if user:
            user.applicant_id = request.session['applicant_id']
            user.passyear = passyear,
            user.course_id = course,
            user.institue_id = institute,
            user.specialization = specialization,
            user.coursetype = coursetype,
            user.qualification = Qualification
            user.save()
            return JsonResponse({"code": 200, "data": None, "msg": "Education detail updated"})
        else:
            user = Education_detail.objects.create(applicant_id=request.session['applicant_id'],
                                                  passyear=passyear,
                                                  course_id=course,
                                                  institue_id=institute,
                                                  specialization=specialization,
                                                  coursetype=coursetype,
                                                  qualification=Qualification)
            user.save()
            return JsonResponse({"code": 200, "data": None, "msg": "education detail created"})




class DashboardView(TemplateView):
    template_name = 'dashboard.html'



class ProfileView(FormView):
    template_name = 'profile.html'
    

    def get_user_data(self):
        user = self.request.user

    def get_context_data(self, **kwargs):
        allInd = Industry.objects.all()
        fa = Functionalarea.objects.all()
        country = Country.objects.all()
        state = State.objects.all()
        language = Language.objects.all()
        institute = Institute.objects.all()
        course = Course.objects.all()
        degree = Degree.objects.all()
        # qualification=Qualification.objects.all()

        context = {'int_list': allInd, 'fa': fa, 'country': country, 'state': state, 'language': language,
                   'institute': institute,
                   'course': course, 'degree': degree,'qualification':''}
        return context


    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()

        messages.success(self.request, _('Profile data has been successfully updated.'))

        return redirect('applicant:dashboard')
