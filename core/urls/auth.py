from django.urls import path, re_path
from django.contrib.auth import views as auth

from ..views import auth as auth_views

auth_urlpatterns = [
    path('/auth/login', auth_views.user_login, name="Auth"),
    path('/auth/logout', auth_views.logout_view, name="Auth"),
    # password reset
    # path('/auth/password-reset', auth.PasswordResetView.as_view(), name="password_reset"),
    # path('/auth/password-reset/done', auth.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('/auth/password-reset/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('/auth/reset/done', auth.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # change password
]
