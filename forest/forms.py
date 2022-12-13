from django import forms
from .models import Forest

class ForestForm(forms.ModelForm):
    class Meta:
        model = Forest
        fields = '__all__'
        labels = {'name': ('Forest')}
        help_texts = {'id': ('Id'),
                      'name': ('Forest'),
                      'domain' : ('Domain'),
                      'status': ('Status') }
        widgets = {'id' : forms.TextInput(attrs={'readonly' : 'readonly'})}