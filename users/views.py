from django.shortcuts import render, redirect
from .forms import UserRegisterForm
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
    profile = Profile.objects.all()

    context = {
        'profile': profile
    }

    return render(request, 'users/profile.html', context)
