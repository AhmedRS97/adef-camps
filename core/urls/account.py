from django.urls import path, re_path

from core.views import (
    signup_manager, signup_trainer, signup_trainee, signup_view,
    login, logout, password_change, password_set,
    account_inactive, email, email_verification_sent,
    confirm_email, password_reset, password_reset_done,
    password_reset_from_key, password_reset_from_key_done,
)

urlpatterns = [
    path("accounts/signup/", signup_view, name="account_signup"),
    path("accounts/signup/trainer/", signup_trainer, name="signup_trainer"),
    path("accounts/signup/trainee/", signup_trainee, name="signup_trainee"),
    path("accounts/signup/manager/", signup_manager, name="signup_manager"),
    path("accounts/login/", login, name="account_login"),
    path("accounts/logout/", logout, name="account_logout"),
    path("accounts/password/change/", password_change, name="account_change_password"),
    path("accounts/password/set/", password_set, name="account_set_password"),
    path("accounts/inactive/", account_inactive, name="account_inactive"),
    path("accounts/email/", email, name="account_email"),
    path(
        "accounts/confirm-email/",
        email_verification_sent,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^accounts/confirm-email/(?P<key>[-:\w]+)/$",
        confirm_email,
        name="account_confirm_email",
    ),
    path(
        "accounts/password/reset/",
        password_reset,
        name="account_reset_password"
    ),
    path(
        "accounts/password/reset/done/",
        password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "accounts/password/reset/key/done/",
        password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
]
