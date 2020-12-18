from django import forms
from django.contrib.auth.models import User
from .models import GitUserInfo

class GitUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class GitUserInfoForm(forms.ModelForm):
	class Meta:
		model = GitUserInfo
		fields = ['UserSite', 'UserPicture']