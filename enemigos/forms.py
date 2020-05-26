from django import forms
from enemigos.models import Enemigo
class EnemigoForm(forms.ModelForm):
    class Meta: 
        model=Enemigo
        fields=['nombre','poder','alias','mundo']
        labels={'Nombre':'Nombre del enemigo', 'Poder':'Poder','Alias':'Alias','Mundo':'Mundo'}
        widget={'Nombre': forms.TextInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })