from django import forms
from .models import FormacaoFlorestal

class FormacaoFlorestalForm(forms.ModelForm):
    class Meta:
        model = FormacaoFlorestal
        fields = '__all__'
        labels = {'nome': ('Formação Florestal')}
        help_texts = {'id': ('Id'),
                      'nome': ('Formação Florestal'),
                      'dominio' : ('Domínio'),
                      'status': ('Status') }
        widgets = {'id' : forms.TextInput(attrs={'readonly' : 'readonly'})}