from allauth.account.forms import SignupForm
from django import forms
from core.models import Manager, Trainer, Trainee, TraineeGroup
from core.models.session import Track


class UserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs |= {
            "class": "test"
        }


class ManagerSignupForm(UserSignupForm):
    title = forms.CharField(label="المسمي", max_length=100)

    def custom_signup(self, request, user):
        user.manager = Manager(title=self.cleaned_data['title'])
        user.manager.save()


class TrainerSignupForm(UserSignupForm):
    title = forms.CharField(label="المسمي", max_length=100)
    bio = forms.CharField(
        label="السيرة الذاتية", widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'السيرة الذاتية'}
        )
    )

    class Meta:
        model = Trainer

    def custom_signup(self, request, user):
        user.trainer = Trainer(
            title=self.cleaned_data['title'],
            bio=self.cleaned_data['bio']
        )
        user.trainer.save()


class TraineeSignupForm(UserSignupForm):
    age = forms.DateTimeField(label="العمر")
    bio = forms.CharField(
        label="السيرة الذاتية", widget=forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': 'السيرة الذاتية'
        })
    )
    group = forms.ModelChoiceField(
        label="المجموعة", queryset=TraineeGroup.objects.all(),
        required=False, blank=True
    )
    track = forms.ModelChoiceField(
        label="التخصص", queryset=Track.objects.all(),
        required=False, blank=True
    )

    def custom_signup(self, request, user):
        user.trainee = Trainee(
            age=self.cleaned_data['age'], bio=self.cleaned_data['bio'],
            group=self.cleaned_data['group'],
            track=self.cleaned_data['track']
        )
        user.trainee.save()
