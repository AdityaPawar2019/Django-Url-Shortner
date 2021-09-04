from django.forms import ModelForm
from django import forms
from .models import Shortner


class ShortenerForm(ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg","placeholder":"Your URL to shorten"}
    ))


    class Meta:
        model = Shortner
        fields = ('long_url',)