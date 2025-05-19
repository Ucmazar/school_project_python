from django.shortcuts import render
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'core/user_list.html', {'users': users})
