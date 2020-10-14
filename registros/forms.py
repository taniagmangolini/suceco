from django import forms
from .models import Registro
from formacaoflorestal.models import FormacaoFlorestal
from especies.models import Especie
from django.forms import ModelChoiceField

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        help_texts = {'id': ('Id'),
                      'especie' : ('Espécie'),
                      'estagio' : ('Estágio Sucessional'),
                      'formacao_florestal': ('Formação Florestal'),
                      'estado' : ('Estado'),
                      'status': ('Status') ,
                      'detalhes' : ('Detalhes'),
                      'referencia': ('Referência')}
        widgets = {'id' : forms.TextInput(attrs={'readonly' : 'readonly'}),
                    'especies_list': forms.HiddenInput  }

        def __init__(self, *args, **kwargs) :
            super(RegistroForm, self).__init__(*args, **kwargs)

            self.fields['formacao_florestal'] = ModelChoiceField(queryset=sorted(FormacaoFlorestal.objects.all(),
                                                                 key=lambda x : x.nome),
                                                                 to_field_name='nome',
                                                                 empty_label="Selecione a Formação Florestal")
            self.fields['especie'] = ModelChoiceField(queryset= sorted(Especie.objects.all(), key=lambda x : x.nome),
                                                      to_field_name='nome',
                                                      empty_label="Selecione a Espécie")
