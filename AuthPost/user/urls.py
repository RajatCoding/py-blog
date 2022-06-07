from django.contrib import admin
from django.urls import path, include
from user import views
from django.contrib.auth import views as auth_views





urlpatterns = [
  
    path('user_signup/', views.user_signup, name='user_sign_up'),
    path('user_login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='user_login'),
    
    path('user_logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name='user_logout'),
    path('edit_profile/<int:pk>', views.ProfileUpdate.as_view(), name='edit_profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name="password_reset"),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name="password_reset_confirm"),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
       template_name="password_reset_complete.html"), name="password_reset_complete"),


]