# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .decorators import user_is_owner_or_admin
from django.core.exceptions import PermissionDenied

# نمایش لیست کاربران
@login_required
def user_list(request):
    if request.user.is_superuser or request.user.is_staff:
        # مدیر یا ادمین: لیست همه کاربران را می‌بیند
        users = UserProfile.objects.all()
    else:
        # غیر مدیر: فقط خودش را می‌بیند
        users = UserProfile.objects.filter(pk=request.user.pk)
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




@user_is_owner_or_admin
@login_required
def profile_view(request):
    user_profile = request.user  # اگر مدل شما UserProfile هست و به عنوان AUTH_USER_MODEL تنظیم شده

    context = {
        'user_profile': user_profile
    }
    return render(request, 'core/profile.html', context)



@login_required
def user_profile_detail(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)
    
    # فقط مدیر می‌تواند پروفایل هر کسی را ببیند و ویرایش کند
    # بقیه فقط پروفایل خودشان را می‌توانند ببینند
    if not (request.user.is_superuser or request.user.is_staff) and request.user.username != username:
        raise PermissionDenied("شما اجازه دسترسی به این صفحه را ندارید.")
    
    return render(request, 'core/profile.html', {'user_profile': user_profile})


@login_required
@user_is_owner_or_admin
def user_profile_edit(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile_detail', username=username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'core/edit_profile.html', {'form': form, 'user_profile': user_profile})



@login_required
def user_profile_delete(request, username):
    user_profile = get_object_or_404(UserProfile, username=username)
    
    if not (request.user.is_superuser or request.user.is_staff) and request.user.username != username:
        raise PermissionDenied("شما اجازه حذف این پروفایل را ندارید.")
    
    if request.method == 'POST':
        user_profile.delete()
        return redirect('user_list')
    
    return render(request, 'core/confirm_delete.html', {'user_profile': user_profile})