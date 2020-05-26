from django import forms
from salvados.models import Salvado
class SalvadoForm(forms.ModelForm):
    class Meta: 
        model=Salvado
        fields=['nombre','nacionalidad','edad']
        labels={'Nombre':'Nombre del enemigo','Nacionalidad':'Nacionalidad','edad':'edad'}
        widget={'Nombre': forms.TextInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })