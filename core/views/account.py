from allauth.account.views import (
    SignupView, LoginView as Login, LogoutView as Logout,
    PasswordChangeView as PasswordChange, PasswordSetView as PasswordSet,
    AccountInactiveView as AccountInactive, EmailView as Email,
    EmailVerificationSentView as EmailVerificationSent,
    ConfirmEmailView as ConfirmEmail, PasswordResetView as PasswordReset,
    PasswordResetDoneView as PasswordResetDone,
    PasswordResetFromKeyDoneView as PasswordResetFromKeyDone,
    PasswordResetFromKeyView as PasswordResetFromKey,
)
from django.shortcuts import redirect

from core.forms import ManagerSignupForm, TrainerSignupForm, TraineeSignupForm


def signup_view(request):
    user_type = request.GET.get('user_type', 'trainee')
    if user_type == 'trainer':
        return redirect('signup_trainer')
    elif user_type == 'trainee':
        return redirect('signup_trainee')
    elif user_type == "manager":
        return redirect('signup_manager')
    return redirect('')


class ManagerSignupView(SignupView):
    form_class = ManagerSignupForm
    template_name = 'account/signup_manager.html'
    success_url = '/'


class TrainerSignupView(SignupView):
    form_class = TrainerSignupForm
    template_name = 'account/signup_trainer.html'
    success_url = '/'


class TraineeSignupView(SignupView):
    form_class = TraineeSignupForm
    template_name = 'account/signup_trainee.html'
    success_url = '/'


class LoginView(Login):
    template_name = 'account/login.html'


class LogoutView(Logout):
    template_name = 'account/logout.html'


class PasswordChangeView(PasswordChange):
    template_name = 'account/password_change.html'


class PasswordSetView(PasswordSet):
    template_name = 'account/password_set.html'


class AccountInactiveView(AccountInactive):
    template_name = 'account/account_inactive.html'


class EmailView(Email):
    template_name = 'account/email.html'


class EmailVerificationSentView(EmailVerificationSent):
    template_name = 'account/verification_sent.html'


class ConfirmEmailView(ConfirmEmail):
    template_name = 'account/email_confirm.html'


class PasswordResetView(PasswordReset):
    template_name = 'account/password_reset.html'


class PasswordResetDoneView(PasswordResetDone):
    template_name = 'account/password_reset_done.html'


class PasswordResetFromKeyDoneView(PasswordResetFromKeyDone):
    template_name = 'account/password_reset_from_key_done.html'


class PasswordResetFromKeyView(PasswordResetFromKey):
    template_name = 'account/password_reset_from_key.html'
