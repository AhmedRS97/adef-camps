from django import forms

from core.models import Track, Session


class TrackForm(forms.ModelForm):
    name = forms.CharField(label="الأسم", max_length=100)
    description = forms.CharField(label="الوصف", widget=forms.Textarea())
    sessions = forms.ModelMultipleChoiceField(
        label="الورشات", queryset=Session.objects.all(), required=False
    )

    class Meta:
        model = Track
        fields = ["name", "description", "sessions"]
