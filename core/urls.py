# core/urls.py
from django.urls import path
from . import views
from .views import profile_view, user_profile_detail

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('create/', views.user_create, name='user_create'),
    path('update/<str:username>/', views.user_update, name='user_update'),
    path('delete/<str:username>/', views.user_delete, name='user_delete'),
    path('profile/', profile_view, name='profile'),
    path('profile/<str:username>/', user_profile_detail, name='profile'),

    path('users/', views.user_list, name='user_list'),
    path('profile/<str:username>/', views.user_profile_detail, name='user_profile_detail'),
    path('profile/<str:username>/edit/', views.user_profile_edit, name='user_profile_edit'),
    path('profile/<str:username>/delete/', views.user_profile_delete, name='user_profile_delete'),

]
