
from dataclasses import fields

from django import forms

from formcrudapp.models import crud

class crudforms(forms.ModelForm):
    class Meta:
        model=crud
        fields="__all__"