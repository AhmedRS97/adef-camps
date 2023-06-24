from django import forms

from core.models import TimeSlot


class TimeSlotForm(forms.ModelForm):
    name = forms.CharField(label="الأسم", max_length=100)

    class Meta:
        model = TimeSlot
        fields = ["name"]
