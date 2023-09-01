from django.db import models

class Proposta(models.Model):
    document = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('análise humana', 'análise humana'), ('Aprovada', 'Aprovada'), ('Negada', 'Negada')], default='análise humana')

    def __str__(self):
        return self.name
    
class CampoPersonalizado(models.Model):
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    valor = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.proposta}"

