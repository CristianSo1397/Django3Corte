from django import forms
from aliados.models import Aliado
class AliadoForm(forms.ModelForm):
    class Meta: 
        model=Aliado
        fields=['nombre','poder','mundo']
        labels={'Nombre':'Nombre del aliado','Poder': 'Poder del aliado','Mundo':'Mundo del aliado'}
        widget={'Nombre': forms.TextInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })