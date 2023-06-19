from django import forms

from core.models import Space


class SpaceForm(forms.ModelForm):
    name = forms.CharField(label="الأسم", max_length=100)

    class Meta:
        model = Space
        fields = ["name"]
