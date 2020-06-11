from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm
from django.views.generic import (DetailView)
from cars.models import DriverUser


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegisterForm()

		args = {'form':form}
		return render(request, 'accounts/register.html', args)


# class ProfileDetail(DetailView):
# 	model = DriverUser

def profile(request):
	args = {'user' : request.user}
	return render(request, 'accounts/profile.html', args)

