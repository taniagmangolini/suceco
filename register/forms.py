from django import forms
from .models import Register
from forest.models import Forest
from species.models import Species
from reference.models import Reference
from django.forms import ModelChoiceField


class RegisterForm(forms.ModelForm):
    class Meta:

        model = Register
        fields = '__all__'
        help_texts = {'id': ('Id'),
                      'species' : ('Species'),
                      'stage' : ('Successional Stage'),
                      'forest': ('Forest'),
                      'state' : ('State'),
                      'status': ('Status'),
                      'latitude' : ('Latitude'),
                      'longitude' : ('Longitude'),
                      'details' : ('Details'),
                      'reference': ('Reference')}
        widgets = {
                   'id' : forms.TextInput(attrs={'readonly' : 'readonly'}),
                   'species_list': forms.HiddenInput,
                   'species': forms.Select(attrs={'style': 'width: 35%'}),
                   'forest': forms.Select(attrs={'style': 'width: 35%'}),
                   'reference': forms.Select(attrs={'style': 'width: 35%'}),
                  }

        def __init__(self, *args, **kwargs) :
            super(RegisterForm, self).__init__(*args, **kwargs)

            self.fields['forest'] = ModelChoiceField(queryset=Forest.objects.all(),
                                                                     to_field_name='name',
                                                                     empty_label="Select the forest")
            self.fields['species'] = ModelChoiceField(queryset=Species.objects.all(),
                                                                       to_field_name='name',
                                                                       empty_label="Select the species")
            self.fields['referemce'] = ModelChoiceField(queryset=Reference.objects.all(),
                                                                           to_field_name='name',
                                                                           empty_label="Select the reference")
            

