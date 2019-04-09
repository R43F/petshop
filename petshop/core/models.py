from django.db import models


class EstoqueManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(nome__icontains=query)
            )


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

    objects = EstoqueManager()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        ordering = ['nome']
