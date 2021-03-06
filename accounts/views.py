from pipes import Template
from pprint import pprint
from django.shortcuts import render
import logging
from django.contrib.auth import login, authenticate
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from accounts.models import User
from .froms import UserCreationForm, UserEditForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.utils.functional import lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
# logger = logging.getLogger(__name__)

class SignupView(FormView):
    template_name = "signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        return response    

class SignupsuccessView(TemplateView):
    template_name = "signup_message.html" 


class UserView(TemplateView):
    model = User
    template_name= "user-detail.html"
  

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class= UserEditForm
    template_name = 'edit-user.html' 
    success_message = "profile updated successfully."
    success_url = reverse_lazy('accounts:userdetail')
    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)
   