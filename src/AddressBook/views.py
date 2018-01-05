from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .forms import RegistrationLoginForm, ContactForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse
from .models import Contact

def home(request):
	return render(request, 'home.html')

def user_page(request):
	return render(request, 'user_page.html')

def register(request):
	
	if request.method == "POST":
		form = RegistrationLoginForm(request.POST)
		if form.is_valid():
			# username = form.cleaned_data['username']
			# password = form.cleaned_data['password']
			username = request.POST['username']
			password = request.POST['password']
			if User.objects.filter(username=username).exists():
				raise forms.ValidationError("Username already taken")
			else:
				User.objects.create_user(username, None, password)
				user = authenticate(request, username=username, password=password)
				auth_login(request, user)
				return redirect(user_page)
				#return HttpResponse("<h1>User successfully registered</h1>")
		else:
			error = form.errors
			for i in error:
				raise forms.ValidationError(error[i][0])
	else:
		form = RegistrationLoginForm()

	return render(request, 'signup_login.html', {'form': form, 'title': 'Register'})

def login(request):

	if request.method == 'POST':
		form = RegistrationLoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth_login(request, user)
				return redirect(user_page)
				#return HttpResponse("<h1>User successfully LoggedIn</h1>")
			else:
				return redirect(login)
				#return HttpResponse("<h1>Wrong Username or Password</h1>")
	else:
		form =RegistrationLoginForm()
		# if request.user.is_authenticated:
		# 	return render()

	return render(request, 'signup_login.html', {'form': form, 'title': 'Login'})

def logout(request):
	auth_logout(request)
	return redirect(home)
	#return HttpResponse("<h1>Logged Out</h1>")

def create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = ContactForm(request.POST)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				form.save()
				return redirect(show)
				#return HttpResponse("<h1>Contact Created</h1>")
		else:
			form = ContactForm()
	else:
		return redirect(login)
		#return HttpResponse("<h1>Login to continue</h1>")

	return render(request, 'create.html', {'form': form, 'title': 'Create'})

def show(request):
	if request.user.is_authenticated:
		#contact_list = get_object_or_404(Contact, user=username)
		contact_list = Contact.objects.filter(user=request.user.id).order_by('id').reverse()
	else:
		return redirect(home)

	return render(request, 'contact_list.html', {'list': contact_list})

def edit(request, contact_id):
	if request.user.is_authenticated:
		instance = get_object_or_404(Contact, pk=contact_id, user=request.user.id)
		if request.method == 'POST':
			form = ContactForm(request.POST, instance=instance)
			if form.is_valid():
				obj = form.save(commit=False)
				obj.user = request.user
				form.save()
				return redirect(show)
		else:
			form = ContactForm(instance=instance)
	else:
		#return HttpResponse("<h1>Login to continue</h1>")
		return redirect(home)
	return render(request, 'create.html', {'form': form, 'title': 'Update'})

def delete(request, contact_id):
	if request.user.is_authenticated:
		instance = get_object_or_404(Contact, pk=contact_id, user=request.user.id)
		instance.delete()
		return redirect(show)
	else:
		return redirect(home)