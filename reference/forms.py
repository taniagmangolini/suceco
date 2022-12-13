from django import forms
from .models import Reference

class ReferenceForm(forms.ModelForm):
    class Meta:

        model = Reference
        fields = '__all__'
        help_texts = {
                      'id': ('Id'),
                      'publication': ('Publication')
                     }

