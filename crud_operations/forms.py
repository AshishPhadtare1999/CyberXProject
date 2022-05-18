from dataclasses import fields
from django import forms
from .models import *

class CustomerForms(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
        }