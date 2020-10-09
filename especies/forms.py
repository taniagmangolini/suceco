from django import forms
from .models import Especie

class EspecieForm(forms.ModelForm):
    class Meta:
        model = Especie
       # fields = ('nome','status'
        fields = '__all__'
        labels = {'nome': ('Espécie')}
        help_texts = {'id': ('Id'), 'nome': ('Espécie'),'status': ('Status') }
        widgets = {'id' : forms.TextInput(attrs={'readonly' : 'readonly'})}