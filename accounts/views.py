from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,f'Account created for {user.username} {user.role}')
            
            if user.role=='applicant':
                return redirect('applicant_dashboard')
            else:
                return redirect('company_dashboard')
    else:
        form=UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form=UserLoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,f'Logged in as {user.username} {user.role}')
            
            if user.role=='applicant':
                return redirect('applicant_dashboard')
            else:
                return redirect('company_dashboard')
        else:
            messages.error(request,'Invalid username or password')
    else:
        form=UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')        