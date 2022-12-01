from django.db import models
from tabnanny import verbose

# Create your models here.

class AlunoModel(models.Model):
    nome = models.CharField('Aluno', max_length=50)
    curso = models.CharField('Curso', max_length=50)
    ano = models.IntegerField('Ano')

    def __str__(self):
        return self.nome + '=>' + str(self.curso)
        
    class Meta:
        verbose_name = 'Aluno'
        verbose_name = 'Alunos'