from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    data = forms.DateField(
        label='Data de Agendamento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Agenda
        fields = ['nome', 'email', 'local', 'opcao', 'data']