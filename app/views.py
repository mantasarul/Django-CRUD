from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .forms import PasswordForm
from .models import Password

# Create your views here.

class PasswordCreateView(CreateView, ListView):
    model = Password
    form_class = PasswordForm
    template_name = "add-password.html"
    success_url = '/'

class PasswordUpdate(UpdateView):
    model = Password
    template_name = 'add-password.html'
    fields = ['username', 'email', 'password']
    success_url = '/'


class PasswordDelete(DeleteView):
    model = Password
    template_name = 'delete.html'
    success_url = '/'


# class PasswordListView(ListView):
#     template_name = 'add-password.html'
#     model = Password
