from .models import movies
from django import forms

class movieForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = ["name", "desc", "year","img"]