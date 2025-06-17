from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Employee
        fields = ["username", "name", "surname", "email", "department", "position"]