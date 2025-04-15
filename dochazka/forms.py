from django import forms

class AttendanceForm(forms.Form):
    passcode = forms.CharField(max_length=7, label="Zadejte svůj kód")