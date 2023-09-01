from django import forms
from .models import CampoPersonalizado

class ConfiguracaoCamposForm(forms.ModelForm):
    class Meta:
        model = CampoPersonalizado
        fields = '__all__'  # Permitir que todos os campos sejam configurados
