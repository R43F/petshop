from django.db import models


class Estoque(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    qtd = models.IntegerField(default=0)
    valor = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Atualizado em', auto_now=True
    )
