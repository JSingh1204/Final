from django import forms

class loginform(forms.Form):
	username=forms.CharField(label="Enter Username",max_length=30)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	Confirm_password= forms.CharField(max_length=32, widget=forms.PasswordInput)


class reg_user(forms.Form):
	username=forms.CharField(label="Enter Username",max_length=30)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
