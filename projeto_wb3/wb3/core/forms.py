from django import forms

class AvaliacaoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    curso = forms.CharField(max_length=50)
    ano = forms.IntegerField()

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
