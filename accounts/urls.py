from django.urls import path
from django.contrib.auth import views as auth_views

from .views import activate_email, signup, update_profile, delete_account

urlpatterns = [
    #auth
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #activate email
    path('activate/<uid>/<token>/', activate_email, name='activate_email'),
    #update profile
    path('update-profile/', update_profile, name='update_profile'),
    #delete account
    path('delete-account/', delete_account, name='delete_account'),
    #password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
