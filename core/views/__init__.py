from .account import (
    ManagerSignupView, TrainerSignupView, TraineeSignupView, signup_view,
    LoginView, LogoutView, PasswordChangeView, PasswordSetView,
    AccountInactiveView, EmailView, EmailVerificationSentView,
    ConfirmEmailView, PasswordResetView, PasswordResetDoneView,
    PasswordResetFromKeyDoneView, PasswordResetFromKeyView,
)
from .session import (
    SessionDetailView, SessionListView, SessionCreateView,
    SessionUpdateView, SessionDeleteView,
)
from .track import (
    TrackDetailView, TrackListView, TrackCreateView,
    TrackUpdateView, TrackDeleteView,
)
from .space import (
    SpaceDetailView, SpaceListView, SpaceCreateView,
    SpaceUpdateView, SpaceDeleteView
)
from .timeslot import (
    TimeSlotDetailView, TimeSlotListView, TimeSlotCreateView,
    TimeSlotUpdateView, TimeSlotDeleteView
)

from .camp import (
    CampDetailView, CampListView, CampCreateView,
    CampUpdateView, CampDeleteView
)

from .group import (
    TraineeGroupDetailView, TraineeGroupListView, TraineeGroupCreateView,
    TraineeGroupUpdateView, TraineeGroupDeleteView
)


signup_manager = ManagerSignupView.as_view()
signup_trainer = TrainerSignupView.as_view()
signup_trainee = TraineeSignupView.as_view()
login = LoginView.as_view()
logout = LogoutView.as_view()
password_change = PasswordChangeView.as_view()
password_set = PasswordSetView.as_view()
account_inactive = AccountInactiveView.as_view()
email = EmailView.as_view()
email_verification_sent = EmailVerificationSentView.as_view()
confirm_email = ConfirmEmailView.as_view()
password_reset = PasswordResetView.as_view()
password_reset_done = PasswordResetDoneView.as_view()
password_reset_from_key = PasswordResetFromKeyView.as_view()
password_reset_from_key_done = PasswordResetFromKeyDoneView.as_view()