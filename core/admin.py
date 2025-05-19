from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class CustomUserAdmin(UserAdmin):
    model = UserProfile
    fieldsets = UserAdmin.fieldsets + (
        ("اطلاعات اضافی", {"fields": ("phone", "address")}),
    )

admin.site.register(UserProfile, CustomUserAdmin)
