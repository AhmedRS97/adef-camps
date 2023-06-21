from allauth.account.forms import SignupForm
from django import forms
from core.models import Manager, Trainer, Trainee, TraineeGroup
from core.models.session import Track


class UserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs |= {
            "class": "form-control"
        }
        self.fields["email"].widget.attrs |= {
            "class": "form-control"
        }
        self.fields["password1"].widget.attrs |= {
            "class": "form-control"
        }
        self.fields["password2"].widget.attrs |= {
            "class": "form-control"
        }



class ManagerSignupForm(UserSignupForm):
    def __init__(self, *args, **kwargs):
        super(ManagerSignupForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs |= {
            "class": "form-control"
        }

    title = forms.CharField(label="المسمي الوظيفى", max_length=100)

    def custom_signup(self, request, user):
        user.manager = Manager(title=self.cleaned_data['title'])
        user.manager.save()


class TrainerSignupForm(UserSignupForm):
    def __init__(self, *args, **kwargs):
        super(TrainerSignupForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs |= {
            "class": "form-control"
        }
        
    title = forms.CharField(label="المسمي الوظيفى", max_length=100)
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

    def __init__(self, *args, **kwargs):
        super(TraineeSignupForm, self).__init__(*args, **kwargs)
        self.fields["age"].widget.attrs |= {
            "class": "form-control"
        }

    username = forms.CharField( widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'}
        ))
    age = forms.DateTimeField(label="العمر")
    bio = forms.CharField(
        label="السيرة الذاتية", widget=forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': 'السيرة الذاتية'
        })
    )
    group = forms.ModelChoiceField(
        label="المجموعة", queryset=TraineeGroup.objects.all(),
        required=False, blank=True,widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
    track = forms.ModelChoiceField(
        label="التخصص", queryset=Track.objects.all(),
        required=False, blank=True,widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    def custom_signup(self, request, user):
        user.trainee = Trainee(
            age=self.cleaned_data['age'], bio=self.cleaned_data['bio'],
            group=self.cleaned_data['group'],
            track=self.cleaned_data['track']
        )
        user.trainee.save()
