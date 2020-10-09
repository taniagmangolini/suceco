from django.db import models
import uuid # Required for unique book instances
from especies.models import Especie
from formacaoflorestal.models import FormacaoFlorestal

class Registro(models.Model) :
    ESTAGIOS = (
        ('pioneira', 'Pioneira'),
        ('secundaria_inicial', 'Secundaria Inicial'),
        ('secundaria_tardia', 'Secundaria Tardia'),
        ('umbrofila', 'Umbrofila'),
        ('secundaria', 'Secundaria')
    )

    STATUS = (
        ('active', 'Ativo'),
        ('inactive', 'Inativo')
    )

    ESTADOS = (
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AP', 'AP'),
        ('AM', 'AM'),
        ('BA', 'BA'),
        ('CE', 'CE'),
        ('DF', 'DF'),
        ('ES', 'ES'),
        ('GO', 'GO'),
        ('MA', 'MA'),
        ('MG', 'MG'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('PA', 'PA'),
        ('PE', 'PE'),
        ('PB', 'PB'),
        ('PI', 'PI'),
        ('PR', 'PR'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RR', 'RR'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('SC', 'SC'),
        ('SE', 'SE'),
        ('SP', 'SP'),
        ('TO', 'TO')
    )

    # Primary
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Foreign Keys
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    formacao_florestal = models.ForeignKey(FormacaoFlorestal, on_delete=models.SET_NULL, null=True)

    estagio = models.CharField(max_length=50, choices=ESTAGIOS)
    estado = models.CharField(max_length=50, choices=ESTADOS)
    status = models.CharField(max_length=15, choices=STATUS, default='Ativo')
    referencia = models.CharField(max_length=1000, default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
