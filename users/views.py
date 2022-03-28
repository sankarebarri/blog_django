from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UpdateProfile, UpdateImageProfile
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} successfully created')
            return redirect('login')

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_profile = UpdateProfile(request.POST, instance=request.user)
        u_image = UpdateImageProfile(request.POST, request.FILES, instance=request.user.profile)
        if u_profile.is_valid() and u_image.is_valid():
            u_profile.save()
            u_image.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile')
    else:
        u_profile = UpdateProfile(instance=request.user)
        u_image = UpdateImageProfile(instance=request.user.profile)
    context = {
        'u_profile': u_profile,
        'u_image':u_image,
    }

    return render(request, 'users/profile.html', context)
