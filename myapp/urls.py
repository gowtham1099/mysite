from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path("logout", views.logout, name='logout'),
    path('main', views.main, name='main'),

    path('reset_password', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='p_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='p_confirm.html'),
         name='password_reset_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='p_complete.html'),
         name='password_reset_complete'),
]
