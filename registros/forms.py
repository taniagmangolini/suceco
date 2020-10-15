from django import forms
from .models import Registro
from formacaoflorestal.models import FormacaoFlorestal
from especies.models import Especie
from django.forms import ModelChoiceField

class RegistroLoteForm(forms.Form):
        referencia =  forms.CharField(max_length=1000)
        detalhes =  forms.CharField(max_length=1000)
        dados_lote =  forms.CharField(widget=forms.Textarea(attrs={'rows': 10}), max_length=1000)


        def __init__(self, *args, **kwargs) :
            super(RegistroLoteForm, self).__init__(*args, **kwargs)

            self.fields['formacao_florestal'] = ModelChoiceField(queryset=FormacaoFlorestal.objects.all(),
                                                                       to_field_name='nome',
                                                                       empty_label="Selecione a Formação Florestal")
            self.fields['estado'] = forms.ChoiceField(choices=(
        ('Selecione o Estado', 'Selecione o Estado'),
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('PA', 'PA'),
        ('PE', 'PE'),
        ('PB', 'PB'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    ))

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
                    'especies_list': forms.HiddenInput                  }

        def __init__(self, *args, **kwargs) :
            super(RegistroForm, self).__init__(*args, **kwargs)

            self.fields['formacao_florestal'] = ModelChoiceField(queryset=FormacaoFlorestal.objects.all(),
                                                                       to_field_name='nome',
                                                                       empty_label="Selecione a Formação Florestal")
            self.fields['especie'] = ModelChoiceField(queryset=Especie.objects.all(),
                                                                       to_field_name='nome',
                                                                       empty_label="Selecione a Espécie")
