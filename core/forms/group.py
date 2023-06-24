from django import forms

from core.models import TraineeGroup


class TraineeGroupForm(forms.ModelForm):
    name = forms.CharField(label="الأسم", max_length=100)
    color = forms.CharField(label="اللون", max_length=20)

    class Meta:
        model = TraineeGroup
        fields = ["name", "color"]
