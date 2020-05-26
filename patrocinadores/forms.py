from django import forms
from patrocinadores.models import Patrocinador
class PatrocinadorForm(forms.ModelForm):
    class Meta: 
        model=Patrocinador
        fields=['nombre','fondos']
        labels={'Nombre':'Nombre del enemigo','Fondos':'Fondos'}
        widget={'Nombre': forms.TextInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })