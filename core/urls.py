# core/urls.py
from django.urls import path
from . import views
from .views import profile_view, user_profile_detail

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<int:pk>/', views.user_update, name='user_update'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('profile/', profile_view, name='profile'),
    path('profile/<str:username>/', user_profile_detail, name='profile'),
]
