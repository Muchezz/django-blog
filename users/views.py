from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm as user_reg

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = user_reg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created!')
            return redirect('login')
    else:
        form = user_reg()
    return render(request, 'users/register.html', {'form': form})
@login_required()
def profile(request):
    return render(request, 'users/profile.html')