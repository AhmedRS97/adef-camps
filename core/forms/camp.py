from django import forms

from core.models import Camp


class DateInput(forms.DateInput):
    input_type = 'date'


class CampForm(forms.ModelForm):
    start_date = forms.DateField(label="تاريخ بداية", widget=DateInput)
    end_date = forms.DateField(label="تاريخ نهاية", widget=DateInput)

    class Meta:
        model = Camp
        fields = ["start_date", "end_date"]
