from django import forms

class ContactForm(forms.Form):
        email = forms.CharField(max_length=1000)
        topic = forms.CharField(max_length=1000)
        message = forms.CharField(widget=forms.Textarea(attrs={'rows' : 10}), max_length=10000)

        def __init__(self, *args, **kwargs) :
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['style'] = 'width:100%;'
            self.fields['topic'].widget.attrs['style'] = 'width:100%;'
            self.fields['message'].widget.attrs['style'] = 'width:100%;'