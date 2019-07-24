from django.shortcuts import render, redirect,render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
from .forms import loginform,reg_user
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# def index(request):
# 	return render(request,'App_1/index.html')


def register(request):
	if request.method=="POST":
		register_form=loginform(request.POST)
		print("Check")
		if register_form.is_valid():
			password1=register_form.cleaned_data['password']
			password2=register_form.cleaned_data['Confirm_password']

			if (password1==password2):
				username=register_form.cleaned_data['username']
				password=register_form.cleaned_data['password']
				print(username)
				print(password)
				user = User.objects.create_user(username,None,password)

				user=authenticate(request,username=username, password=password)

				login(request,user)
				# print("Check")
				print("Final Check")
				return render(request,'App_1/index.html')

	else:
		register_form=loginform()

	result={'register_form':register_form}

	return render(request,'Registration/register.html',result)

def user_logged(request):
	if request.method=="POST":
		register_form=reg_user(request.POST)
		if register_form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(request,username=username, password=password)
			if user is not None:
				login(request,user)
				# print("Check")
				print("Final Check")
				user.save()

				#return  render(request,'App_1/index.html')

				# messages.success(request,"User Logged In")
				return HttpResponseRedirect('welcome')
			else:
				print("Wrong")

	else:

		register_form=reg_user()

	result={'register_form':register_form}

	return render(request,'Registration/login.html',result)


def user_out(request):
	if request.method =="POST":
		logout(request)
		return render(request,'App_1/logout.html')
	else:
		#return HttpResponseNotFound('<h1>Page not found</h1>')
		return HttpResponse(status=404)

@login_required
def welcome(request):
	if request.method=="GET":
		return render(request,'App_1/index.html')
	else:
		return HttpResponse("Check Done")




