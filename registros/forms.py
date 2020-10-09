from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        help_texts = {'id': ('Id'),
                      'especie' : ('Espécie'),
                      'estagio' : ('Estágio Sucessional'),
                      'formacao_florestal': ('Formação Florestal'),
                      'estado' : ('Estado'),
                      'status': ('Status') }
        widgets = {'id' : forms.TextInput(attrs={'readonly' : 'readonly'})}