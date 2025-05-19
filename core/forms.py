# core/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'phone',  'address', 'email', 'username', 'password']  # به‌جای user
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'email': 'ایمیل',
            'phone': 'شماره تماس',
            'address': 'آدرس',
            'password': 'کلمه عبور'
        }
