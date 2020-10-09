from django.db import models
import uuid # Required for unique book instances

class FormacaoFlorestal(models.Model) :
    STATUS = (
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo')
    )

    DOMINIOS = (
        ('Amazonia', 'Amazonia'),
        ('Mata Atlantica', 'Mata Atlantica'),
        ('Caatinga', 'Caatinga'),
        ('Cerrado', 'Cerrado'),
        ('Pantanal', 'Pantanal'),
        ('Pradarias', 'Pradarias'),
        ('', '')
    )

    # Primary
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nome = models.CharField(max_length=500, unique=True)
    dominio = models.CharField(max_length=100, choices=DOMINIOS)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Ativo')
