from django import forms

from .models import ParametersModel


class SurveyForm(forms.ModelForm):
    class Meta:
        model = ParametersModel
