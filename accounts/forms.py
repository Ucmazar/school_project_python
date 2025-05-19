from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import UserProfile  # مدل کاربر سفارشی خودت

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomAuthenticationForm(AuthenticationForm):
    # اینجا اگر بخوای می‌تونی فیلدها رو سفارشی کنی
    pass


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="تأیید رمز عبور",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = UserProfile
        fields = ("username", "email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور و تأیید آن مطابقت ندارند.")
        return password2