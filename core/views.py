# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# نمایش لیست کاربران
def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'core/user_list.html', {'users': users})

# ایجاد کاربر جدید
def user_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm()
    return render(request, 'core/user_form.html', {'form': form})

# ویرایش کاربر
def user_update(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'core/user_form.html', {'form': form})

# حذف کاربر
def user_delete(request, pk):
    user_profile = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user_profile.delete()
        return redirect('user_list')
    return render(request, 'core/user_confirm_delete.html', {'user_profile': user_profile})




@login_required
def profile_view(request):
    user_profile = request.user  # اگر مدل شما UserProfile هست و به عنوان AUTH_USER_MODEL تنظیم شده

    context = {
        'user_profile': user_profile
    }
    return render(request, 'core/profile.html', context)


def user_profile_detail(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)
    return render(request, 'core/profile.html', {'user_profile': user_profile})