from django.urls import path
from django.contrib.auth import views as auth_views  # Keep this if needed elsewhere
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('sponsor-front/', views.sponsor_front, name='sponsor_front'),
    path('sponsor/create/', views.create_sponsorship, name='create_sponsorship'),
    path('sponsor/profile/', views.update_sponsor_profile, name='update_sponsor_profile'),
    path('participant-dashboard/', views.participant_dashboard, name='participant_dashboard'),
]
