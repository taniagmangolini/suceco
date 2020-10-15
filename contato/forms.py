from django import forms

class ContatoForm(forms.Form):
        email = forms.CharField(max_length=1000)
        assunto = forms.CharField(max_length=1000)
        mensagem = forms.CharField(widget=forms.Textarea(attrs={'rows' : 10}), max_length=10000)

        def __init__(self, *args, **kwargs) :
            super(ContatoForm, self).__init__(*args, **kwargs)