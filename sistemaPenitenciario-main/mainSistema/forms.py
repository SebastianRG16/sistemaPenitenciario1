from django import forms
from .models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'