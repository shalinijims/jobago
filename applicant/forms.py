from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import *
from django.contrib.auth.hashers import make_password



class SignUpForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields ={'email','mobile','password'}

    email = forms.EmailField(label=_('Email'), help_text=_('Required.'),widget=forms.TextInput(attrs={'placeholder': 'Email ID'}))
    password = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
                                help_text=_("Enter the same password as above, for verification."))
    mobile=forms.CharField(label=_('Mobile'),help_text=_('Required'),widget=forms.TextInput(attrs={'placeholder':'Mobile'}),max_length=10)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Password Mismatch'))
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        user = Applicant.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('Email Already Exists.'))
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.mobile=self.cleaned_data['mobile']
        user.password=make_password(self.cleaned_data['password'])
       # user.set_password(self.cleaned_data.get["password"])
        user.is_active=1
        user.profile_complete=0
        if commit:
            user.save()

        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'), help_text=_('Required.'),
                             widget=forms.TextInput(attrs={'placeholder': 'Email ID'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = Applicant.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address.'))
        return email




class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Last name'), max_length=150, required=False)


class DashboardFormView(forms.Form):
    first_name = forms.CharField(label=_('First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Last name'), max_length=150, required=False)
    email = forms.EmailField(label=_('Email'))
    userid = forms.CharField(label=_('id'), max_length=150, required=False)




