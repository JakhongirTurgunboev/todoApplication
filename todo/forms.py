from django import forms
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            "Age cannot be negative"
        )


class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    age = forms.IntegerField(validators=[validate_positive])
    task = forms.CharField(label="Task", max_length=500)
    deadline = forms.DateField(label="Deadline")
