from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    semestre = models.IntegerField()
    curso = models.CharField(max_length=50)


    class Meta:
        ordering = ('nome', )
    
    def __str__(self):
        return self.nome


class Sala(models.Model):
    disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, related_name='professor', on_delete=models.CASCADE)
    alunos = models.ForeignKey(Aluno, related_name='alunos', on_delete=models.CASCADE)


    class Meta:
        ordering = ('disciplina', )

    def __str__(self):
        return self.disciplina


class Atividade(models.Model):
    sala = models.ForeignKey(Sala, related_name='Disciplina', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    data_criado = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(null=False)


    class Meta:
        ordering = ('titulo', )

    def __str__(self):
        return self.titulo