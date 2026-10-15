from django import forms
from .models import ObjetoPerdido

class ObjetoForm(forms.ModelForm):
    nombre = forms.CharField(label='Objeto', min_length=3, max_length=60)
    descripcion = forms.CharField(label='Descripcion', min_length=10, max_length=500)
    lugar_hallazgo = forms.CharField(label='Lugar donde se encontro', min_length=3, max_length=80)
    encontrado_por = forms.CharField(label='Funcionario que lo encontro', min_length=3, max_length=60)
    correo_funcionario = forms.EmailField(label='Correo del funcionario')
    valor_estimado = forms.IntegerField(label='Valor estimado ($)', min_value=0, max_value=5000000)

    class Meta:
        model = ObjetoPerdido
        fields = '__all__'

    def clean_encontrado_por(self):
        inputFuncionario = self.cleaned_data['encontrado_por']
        if inputFuncionario.find(' ') == -1:
            raise forms.ValidationError('Escriba el nombre y el apellido del funcionario.')
        return inputFuncionario

    def clean_correo_funcionario(self):
        inputCorreo = self.cleaned_data['correo_funcionario']
        if inputCorreo.find('@cordilleraazul.cl') == -1:
            raise forms.ValidationError('El correo debe ser institucional (@cordilleraazul.cl).')
        return inputCorreo
