from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _

from employee.models import Employee
from .forms import RegistrationForm, LoginForm


def home_page_view(request):
    return render(request, 'general/home_page.html')


def registration_form_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            Employee.objects.create_user(username, email, password,
                                         last_name=last_name,
                                         first_name=first_name)
            return redirect('general:profile')
    else:
        form = RegistrationForm()
    return render(request, 'general/registration.html', {'form': form.as_p()})


def login_form_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('general:profile')
            else:
                messages.error(request, _("Wrong username or password"))
                return redirect('general:login')
    else:
        form = LoginForm()
    return render(request, 'general/login.html', {'form': form})


def profile_view(request):
    current_user = request.user
    return render(request, 'general/profile.html', {
        'user': current_user
    })
