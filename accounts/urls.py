from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
# from django.contrib.auth import views as auth_views




app_name = 'accounts'

urlpatterns = [
	path('signup/', views.signup_view, name='signup'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('profile/', views.profile_view, name='profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change-password/', views.change_password, name='change_password'),
	path('update_profile/', views.update_profile, name='update_profile'),
	path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
	path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),



] 


