from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm as user_reg

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = user_reg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = user_reg()
    return render(request, 'users/register.html', {'form': form})