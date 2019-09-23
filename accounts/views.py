from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from . models import UserProfile, Profile
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm, EditProfileForm, UserEditForm, ProfileEditForm


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Profile.objects.create(user=new_user)
            return redirect('list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#Log in the User
			user = form.get_user()
			login(request, user)
			return redirect('accounts:profile')
	else:
		form = AuthenticationForm()	
	return render(request, 'accounts/login.html', {'form':form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)
	return redirect('home')


def profile_view(request):
	args = {'user': request.user}
	return render(request, 'accounts/profile.html', args)


def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('accounts:edit_profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request, 'accounts/edit_profile.html', args)			

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('accounts:profile')
		else:
			return redirect('accounts:change-password')	

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request, 'accounts/change_password.html', args)		



@login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('accounts:profile')
       
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })