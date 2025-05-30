from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # بعدا پروفایل رو می‌سازیم
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')  # صفحه پروفایل
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def profile_view(request):
    user = request.user  # کاربر وارد شده
    return render(request, 'core/profile.html', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('login')  # یا هر صفحه‌ای که می‌خوای بعد خروج بری


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # یا هر صفحه‌ای که می‌خوای
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})