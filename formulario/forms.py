from django import forms

from .models import Personas


class PersonasForm(forms.ModelForm):

    class Meta:
        model = Personas
        fields = ("name",)
