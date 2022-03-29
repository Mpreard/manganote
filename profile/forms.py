from distutils import dep_util
from mimetypes import init
from typing import Any
from django import forms
from django.core.validators import RegexValidator

password_validator = RegexValidator(
    "^(?=.{10,}$)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?\W).*$",
    "Your password should contain at least : 8 characters, one lowercase, one uppercase, one digit and one special character.",
)
name_validator = RegexValidator(
    "^[a-zA-Z]+$", "Your first and last name should contain only characters."
)
phone_validator = RegexValidator("^[0-9]{10}$", "Wrong phone format.")


class UpdateUserForm(forms.Form):
    password = forms.CharField(required=False, validators=[password_validator])
    first_name = forms.CharField(required=False, validators=[name_validator])
    last_name = forms.CharField(required=False, validators=[name_validator])
    telephone = forms.CharField(required=False, validators=[phone_validator])
