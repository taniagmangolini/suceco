from django import forms
from .models import Species

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = '__all__'
        labels = {'name': ('Species')}
        help_texts = {'id': ('Id'), 'species': ('species'),'status': ('Status') }
        widgets = {'id' : forms.TextInput(attrs={'readonly' : 'readonly'})}