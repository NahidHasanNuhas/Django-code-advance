from django.shortcuts import render
from .forms import GitUserForm, GitUserInfoForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'GitApp/index.html', {})

def register(request):
	registered = False

	if request.method == 'POST':
		UserForm = GitUserForm(request.POST)
		ProfileForm = GitUserInfoForm(request.POST)

		if UserForm.is_valid() and ProfileForm.is_valid():
			user = UserForm.save()
			user.set_password(user.password)
			user.save()

			profile = ProfileForm.save(commit=False)
			profile.user = user

			if 'UserPicture' in request.FILES:
				profile.UserPicture = request.FILES['UserPicture']
			profile.save()

			registered = True
		else:
			print(UserForm.errors, ProfileForm.errors)
	
	else:
		UserForm = GitUserForm()
		ProfileForm = GitUserInfoForm()
	
	context_dict = {
		'registered': registered,
		'UserForm': UserForm,
		'ProfileForm': ProfileForm,
	}
	return render(request, 'GitApp/registration.html', context_dict)

def UserLogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		User = authenticate(username=username, password=password)

		if User:
			if User.is_active:
				login(request, User)
				return render(request, 'GitApp/afterlogin.html', {'UserName': username})
			else:
				return HttpResponse('<h1>ACCOUNT NOT ACTIVE</h1>')
		else:
			print('Did you tried to login with:')
			print(f'username: {username}, password: {password}')
			return HttpResponse('INVALID DETAILS')
	else:
		return render(request, 'GitApp/login.html',)

@login_required
def UserLogout(request):
	logout(request)
	return redirect('GitApp:UserLogin')
