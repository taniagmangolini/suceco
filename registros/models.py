from django.db import models
import uuid
from especies.models import Especie
from formacaoflorestal.models import FormacaoFlorestal
from suceco._constants import ESTAGIOS, STATUS, ESTADOS

class Registro(models.Model) :

    # Primary
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Foreign Keys
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    formacao_florestal = models.ForeignKey(FormacaoFlorestal, on_delete=models.SET_NULL, null=True)

    # Other fields
    estagio = models.CharField(max_length=50, choices=ESTAGIOS)
    estado = models.CharField(max_length=50, choices=ESTADOS)
    status = models.CharField(max_length=15, choices=STATUS, default='Ativo')
    referencia = models.CharField(max_length=1000, default='')
    detalhes = models.CharField(max_length=1000, default= '')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return '-'.join([str(self.id), self.especie.nome, self.formacao_florestal.nome])
