from django import forms

from core.models import Trainer, Track, Session


class SessionForm(forms.ModelForm):
    title = forms.CharField(label="العنوان", max_length=100)
    description = forms.CharField(label="الوصف", widget=forms.Textarea())
    capacity = forms.IntegerField(label="العدد", min_value=1)
    link = forms.URLField(label="الرابط", required=False)
    trainer = forms.ModelChoiceField(
        label="المدرب", queryset=Trainer.objects.all(), required=False
    )
    track = forms.ModelChoiceField(
        label="التخصص", queryset=Track.objects.all(), required=False
    )

    class Meta:
        model = Session
        fields = [
            "title", "description", "capacity", "link",
            "trainer", "track",
        ]
