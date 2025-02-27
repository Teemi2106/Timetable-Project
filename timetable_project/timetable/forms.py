from django import forms
from .models import Department, Level

class TimetableForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), label="Department")
    level = forms.ModelChoiceField(queryset=Level.objects.all(), label="Level")
